import { computed, type Ref } from 'vue';
import { useMutation, useQuery } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import type { Level } from '@/utils/levels';
import type { PlacementAnswer, PlacementResult, PlacementTest } from '@/types/placement';

export function usePlacementQuestions(languageId: Ref<string>, level: Ref<Level>) {
  return useQuery({
    queryKey: computed(() => ['placement', languageId.value, level.value]),
    queryFn: ({ signal }) =>
      request<PlacementTest>(
        'GET',
        `/languages/${languageId.value}/placement-test/${level.value}`,
        undefined,
        { signal },
      ),
    gcTime: 0,
    staleTime: Infinity,
    retry: false,
    refetchOnWindowFocus: false,
  });
}

interface SubmitPlacementVariables {
  languageId: string;
  level: Level;
  answers: PlacementAnswer[];
}

export function useSubmitPlacement() {
  return useMutation({
    mutationFn: ({ languageId, level, answers }: SubmitPlacementVariables) =>
      request<PlacementResult>(
        'POST',
        `/languages/${languageId}/placement-test/${level}`,
        { answers },
      ),
  });
}
