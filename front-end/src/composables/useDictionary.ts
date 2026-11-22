import { computed, type Ref } from 'vue';
import { useQuery } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import type { DictionaryEntry } from '@/types/lingq';

export function useDictionary(term: Ref<string>) {
  return useQuery({
    queryKey: computed(() => ['dictionary', term.value]),
    queryFn: ({ signal }) =>
      request<DictionaryEntry>('GET', `/dictionary/lookup?term=${encodeURIComponent(term.value)}`, undefined, { signal }),
    enabled: computed(() => term.value.length > 0),
    staleTime: 60 * 60_000,
    retry: false,
  });
}
