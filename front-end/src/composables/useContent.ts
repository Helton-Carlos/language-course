import { computed, type Ref } from 'vue';
import { useQuery } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import type { Phrase, PodcastEpisode } from '@/types/content';

type LanguageId = Ref<string | null | undefined>;

export function usePodcasts(languageId: LanguageId) {
  return useQuery({
    queryKey: computed(() => ['podcasts', languageId.value]),
    queryFn: ({ signal }) =>
      request<PodcastEpisode[]>('GET', `/languages/${languageId.value}/podcasts`, undefined, { signal }),
    enabled: computed(() => !!languageId.value),
    staleTime: 10 * 60_000,
  });
}

export function usePhrases(languageId: LanguageId) {
  return useQuery({
    queryKey: computed(() => ['phrases', languageId.value]),
    queryFn: ({ signal }) =>
      request<Phrase[]>('GET', `/languages/${languageId.value}/phrases`, undefined, { signal }),
    enabled: computed(() => !!languageId.value),
    staleTime: 10 * 60_000,
  });
}
