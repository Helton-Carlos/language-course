import re
from datetime import UTC, date, datetime, timedelta, timezone

KNOWN_STATUS = 5
MIN_STATUS = 1
DAILY_GOAL = 10
REVIEW_BATCH_SIZE = 20
STREAK_LOOKBACK_DAYS = 400
LOCAL_TIMEZONE = timezone(timedelta(hours=-3))

REVIEW_INTERVALS = {
    1: timedelta(days=1),
    2: timedelta(days=2),
    3: timedelta(days=4),
    4: timedelta(days=8),
}

_EDGE_PUNCTUATION = ' \t\r\n.,;:!?"()[]{}<>«»“”‘…—–-'
_WORD_PATTERN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)*")


def normalize_term(value: str) -> str:
    cleaned = re.sub(r"\s+", " ", value.replace("’", "'").replace("‘", "'"))
    return cleaned.strip(_EDGE_PUNCTUATION).lower()


def count_words(text: str) -> int:
    return len(_WORD_PATTERN.findall(text.replace("’", "'")))


def now_utc() -> datetime:
    return datetime.now(UTC)


def today_local() -> date:
    return datetime.now(LOCAL_TIMEZONE).date()


def next_review_for(status: int, moment: datetime) -> datetime | None:
    interval = REVIEW_INTERVALS.get(status)
    return None if interval is None else moment + interval
