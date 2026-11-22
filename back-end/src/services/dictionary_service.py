import asyncio
import re
from urllib.parse import quote

import httpx

from schemas.dictionary import DictionaryEntryOut

TRANSLATE_URL = "https://api.mymemory.translated.net/get"
DEFINITION_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
REQUEST_TIMEOUT = 5.0
CACHE_LIMIT = 2048
MAX_SUGGESTIONS = 4
MIN_MATCH_SCORE = 0.5

_cache: dict[str, DictionaryEntryOut] = {}


class DictionaryService:
    async def lookup(self, term: str) -> DictionaryEntryOut:
        cached = _cache.get(term)
        if cached is not None:
            return cached
        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
            suggestions, details = await asyncio.gather(
                self._translate(client, term),
                self._define(client, term),
            )
        entry = DictionaryEntryOut(
            term=term,
            translation=suggestions[0] if suggestions else None,
            suggestions=suggestions,
            definition=details[0],
            phonetic=details[1],
        )
        if suggestions or details[0]:
            if len(_cache) >= CACHE_LIMIT:
                _cache.clear()
            _cache[term] = entry
        return entry

    @staticmethod
    async def _translate(client: httpx.AsyncClient, term: str) -> list[str]:
        try:
            response = await client.get(TRANSLATE_URL, params={"q": term, "langpair": "en|pt-BR"})
            response.raise_for_status()
            payload = response.json()
            if int(payload.get("responseStatus", 0)) != 200:
                return []
            matches = payload.get("matches") or []
        except (httpx.HTTPError, ValueError, TypeError):
            return []
        scores: dict[str, float] = {}
        has_digit = bool(re.search(r"\d", term))
        for match in matches:
            try:
                text = " ".join(str(match["translation"]).split()).strip(" .,;")
                score = float(match["match"])
            except (KeyError, TypeError, ValueError):
                continue
            if score < MIN_MATCH_SCORE or not text or len(text) > 100:
                continue
            if text.lower() == term.lower() or "MYMEMORY" in text.upper():
                continue
            if not has_digit and re.search(r"\d", text):
                continue
            key = text.lower()
            scores[key] = scores.get(key, 0.0) + score
        ranked = sorted(scores, key=lambda key: scores[key], reverse=True)
        return ranked[:MAX_SUGGESTIONS]
    @staticmethod
    async def _define(client: httpx.AsyncClient, term: str) -> tuple[str | None, str | None]:
        if " " in term:
            return None, None
        try:
            response = await client.get(f"{DEFINITION_URL}{quote(term, safe='')}")
            if response.status_code != 200:
                return None, None
            entry = response.json()[0]
            phonetic = entry.get("phonetic") or next(
                (item["text"] for item in entry.get("phonetics", []) if item.get("text")),
                None,
            )
            definition = next(
                (
                    f"({meaning['partOfSpeech']}) {item['definition']}"
                    for meaning in entry.get("meanings", [])
                    for item in meaning.get("definitions", [])
                    if item.get("definition")
                ),
                None,
            )
        except (httpx.HTTPError, ValueError, KeyError, IndexError, TypeError):
            return None, None
        return definition, phonetic
