import { computed } from 'vue';
import { useQuery } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import type { Language } from '@/types/language';

export const LANGUAGES_QUERY_KEY = ['languages'] as const;

export function useLanguages() {
  const query = useQuery({
    queryKey: LANGUAGES_QUERY_KEY,
    queryFn: ({ signal }) => request<Language[]>('GET', '/languages', undefined, { signal }),
    staleTime: 1000 * 60 * 10,
  });

  const languages = computed(() => query.data.value ?? []);

  return { ...query, languages };
}
