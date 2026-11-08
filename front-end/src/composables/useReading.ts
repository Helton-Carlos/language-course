import { computed, type Ref } from 'vue';
import { useQuery } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import { useCurrentUser } from '@/composables/useCurrentUser';
import type { ReadingSituation, ReadingText, ReadingTheme } from '@/types/reading';

const CONTENT_STALE_TIME = 10 * 60_000;

export function useReadingThemes() {
  return useQuery({
    queryKey: ['reading', 'themes'],
    queryFn: ({ signal }) => request<ReadingTheme[]>('GET', '/reading/themes', undefined, { signal }),
    staleTime: CONTENT_STALE_TIME,
  });
}

export function useReadingSituations(theme: Ref<string>) {
  return useQuery({
    queryKey: computed(() => ['reading', 'situations', theme.value]),
    queryFn: ({ signal }) =>
      request<ReadingSituation[]>('GET', `/reading/themes/${theme.value}/situations`, undefined, { signal }),
    enabled: computed(() => !!theme.value),
    staleTime: CONTENT_STALE_TIME,
  });
}

export function useReadingText(theme: Ref<string>, situation: Ref<string>) {
  const { data: user } = useCurrentUser();

  return useQuery({
    queryKey: computed(() => ['reading', 'text', user.value?.id, user.value?.level, theme.value, situation.value]),
    queryFn: ({ signal }) =>
      request<ReadingText>('GET', `/reading/themes/${theme.value}/situations/${situation.value}`, undefined, { signal }),
    enabled: computed(() => !!theme.value && !!situation.value),
    staleTime: CONTENT_STALE_TIME,
  });
}
