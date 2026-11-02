import { useQuery } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import type { User } from '@/types/user';

export const CURRENT_USER_QUERY_KEY = ['me'] as const;

export const currentUserQuery = {
  queryKey: CURRENT_USER_QUERY_KEY,
  queryFn: () => request<User | null>('GET', '/auth/me'),
  staleTime: 60_000,
  retry: false,
} as const;

export function hasCompleteProfile(user: User): boolean {
  return user.language_id !== null && user.level !== null;
}

export function useCurrentUser() {
  return useQuery(currentUserQuery);
}
