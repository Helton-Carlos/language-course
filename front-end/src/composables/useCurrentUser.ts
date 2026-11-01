import { useQuery } from '@tanstack/vue-query';
import { ApiError, request } from '@/composables/useApi';
import type { User } from '@/types/user';

export const CURRENT_USER_QUERY_KEY = ['me'] as const;

async function fetchCurrentUser(): Promise<User | null> {
  try {
    return await request<User>('GET', '/auth/me');
  } catch (error) {
    if (error instanceof ApiError && error.status === 401) return null;
    throw error;
  }
}

export const currentUserQuery = {
  queryKey: CURRENT_USER_QUERY_KEY,
  queryFn: fetchCurrentUser,
  staleTime: 60_000,
  retry: false,
} as const;

export function hasCompleteProfile(user: User): boolean {
  return user.language_id !== null && user.level !== null;
}

export function useCurrentUser() {
  return useQuery(currentUserQuery);
}
