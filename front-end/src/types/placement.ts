import type { Level } from '@/utils/levels';

export interface PlacementOption {
  index: number;
  text: string;
}

export interface PlacementQuestion {
  id: string;
  prompt: string;
  options: PlacementOption[];
}

export interface PlacementTest {
  level: Level;
  questions: PlacementQuestion[];
}

export interface PlacementAnswer {
  question_id: string;
  option_index: number;
}

export interface PlacementResult {
  level: Level;
  correct: number;
  total: number;
  passed: boolean;
  next_level: Level | null;
  result_level: Level | null;
}
