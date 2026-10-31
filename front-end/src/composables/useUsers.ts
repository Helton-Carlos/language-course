import { computed } from 'vue';
import { useQuery } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import type { User } from '@/types/user';

export const USERS_QUERY_KEY = ['users'] as const;

export function useUsers() {
  const query = useQuery({
    queryKey: USERS_QUERY_KEY,
    queryFn: ({ signal }) => request<User[]>('GET', '/users', undefined, { signal }),
    staleTime: 1000 * 60 * 5,
  });

  const users = computed(() => query.data.value ?? []);

  return { ...query, users };
}
