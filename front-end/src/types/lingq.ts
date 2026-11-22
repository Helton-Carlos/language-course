export type WordStatus = 1 | 2 | 3 | 4 | 5;

export interface VocabularyItem {
  id: string;
  term: string;
  meaning: string;
  context: string | null;
  status: WordStatus;
  review_count: number;
  next_review_at: string | null;
  created_at: string;
  updated_at: string;
}

export interface VocabularyMapItem {
  term: string;
  meaning: string;
  status: WordStatus;
}

export interface VocabularyPayload {
  term: string;
  meaning: string;
  context?: string;
  status: WordStatus;
}

export interface VocabularyUpdatePayload {
  meaning?: string;
  status?: WordStatus;
}

export interface VocabularyFilters {
  status: WordStatus | null;
  search: string;
}

export interface DictionaryEntry {
  term: string;
  translation: string | null;
  suggestions: string[];
  definition: string | null;
  phonetic: string | null;
}

export interface LessonSummary {
  id: string;
  title: string;
  preview: string;
  word_count: number;
  created_at: string;
}

export interface Lesson {
  id: string;
  title: string;
  body: string;
  word_count: number;
  created_at: string;
}

export interface LessonPayload {
  title: string;
  body: string;
}

export interface DayActivity {
  day: string;
  lingqs_created: number;
  reviews: number;
  words_read: number;
}

export interface StatusCount {
  status: WordStatus;
  count: number;
}

export interface Stats {
  daily_goal: number;
  today: DayActivity;
  today_progress: number;
  streak: number;
  known_words: number;
  total_items: number;
  due_count: number;
  words_read_total: number;
  by_status: StatusCount[];
  last_days: DayActivity[];
}
