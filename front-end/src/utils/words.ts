import type { WordStatus } from '@/types/study';

export const WORD_STATUSES: readonly WordStatus[] = [1, 2, 3, 4, 5];
export const KNOWN_STATUS: WordStatus = 5;
export const MAX_PHRASE_WORDS = 8;

export const STATUS_LABELS: Record<WordStatus, string> = {
  1: 'Novo',
  2: 'Reconhecido',
  3: 'Familiar',
  4: 'Aprendido',
  5: 'Conhecido',
};

export const STATUS_BADGE_CLASSES: Record<WordStatus, string> = {
  1: 'bg-amber-300 text-tertiary',
  2: 'bg-amber-200 text-tertiary',
  3: 'bg-amber-100 text-tertiary',
  4: 'bg-yellow-50 text-tertiary ring-1 ring-amber-200',
  5: 'bg-quinary/20 text-tertiary',
};

export const STATUS_WORD_CLASSES: Record<WordStatus, string> = {
  1: 'bg-amber-300',
  2: 'bg-amber-200',
  3: 'bg-amber-100',
  4: 'border-b-2 border-amber-300',
  5: '',
};

export const UNKNOWN_WORD_CLASS = 'bg-sky-200';

export type TextToken =
  | { kind: 'word'; text: string; term: string }
  | { kind: 'text'; text: string };

const WORD_PATTERN = /[A-Za-z]+(?:['’][A-Za-z]+)*/g;

export function normalizeTerm(value: string): string {
  return value
    .replace(/[’‘]/g, "'")
    .replace(/\s+/g, ' ')
    .replace(/^[\s.,;:!?"()[\]{}<>«»“”‘…—–-]+|[\s.,;:!?"()[\]{}<>«»“”‘…—–-]+$/g, '')
    .toLowerCase();
}

export function tokenizeLine(line: string): TextToken[] {
  const tokens: TextToken[] = [];
  let cursor = 0;
  for (const match of line.matchAll(WORD_PATTERN)) {
    const start = match.index ?? 0;
    if (start > cursor) tokens.push({ kind: 'text', text: line.slice(cursor, start) });
    tokens.push({ kind: 'word', text: match[0], term: normalizeTerm(match[0]) });
    cursor = start + match[0].length;
  }
  if (cursor < line.length) tokens.push({ kind: 'text', text: line.slice(cursor) });
  return tokens;
}

export function splitParagraphs(body: string): string[] {
  return body
    .split(/\n+/)
    .map((paragraph) => paragraph.trim())
    .filter(Boolean);
}

export function extractTerms(body: string): string[] {
  const terms = new Set<string>();
  for (const match of body.matchAll(WORD_PATTERN)) terms.add(normalizeTerm(match[0]));
  return [...terms];
}

export function countWords(body: string): number {
  return body.match(WORD_PATTERN)?.length ?? 0;
}

export function isValidTerm(term: string): boolean {
  return term.length > 0 && term.length <= 100 && /[a-z]/.test(term);
}
