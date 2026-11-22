import { computed } from 'vue';
import { useMutation, useQuery, useQueryClient } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import { useCurrentUser } from '@/composables/useCurrentUser';
import type { Stats } from '@/types/study';

export function useStats() {
  const { data: user } = useCurrentUser();
  return useQuery({
    queryKey: computed(() => ['stats', user.value?.id]),
    queryFn: ({ signal }) => request<Stats>('GET', '/stats', undefined, { signal }),
    enabled: computed(() => !!user.value),
    staleTime: 30_000,
  });
}

export function useRecordReading() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (words: number) => request<void>('POST', '/stats/reading', { words }),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['stats'] }),
  });
}
