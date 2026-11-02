import type { Language } from '@/types/language';
import type { Level } from '@/utils/levels';

export const ROLES = ['admin', 'user'] as const;
export type Role = (typeof ROLES)[number];

export interface User {
  id: string;
  name: string;
  last_name?: string;
  email: string;
  role: Role;
  language_id: string | null;
  language: Language | null;
  level: Level | null;
}

export interface CreateUserPayload {
  name: string;
  last_name?: string;
  email: string;
  password: string;
}

export interface RegisterPayload extends CreateUserPayload {
  password_confirm: string;
}

export interface LoginPayload {
  email: string;
  password: string;
}

export interface ProfilePayload {
  level: Level;
}
