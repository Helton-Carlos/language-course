import { computed, type Ref } from 'vue';
import { keepPreviousData, useMutation, useQuery, useQueryClient } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import { useCurrentUser } from '@/composables/useCurrentUser';
import { MESSAGES } from '@/utils/message';
import type {
  VocabularyFilters,
  VocabularyItem,
  VocabularyMapItem,
  VocabularyPayload,
  VocabularyUpdatePayload,
} from '@/types/study';

const VOCABULARY_PAGE_SIZE = 200;

function useUserId() {
  const { data: user } = useCurrentUser();
  return computed(() => user.value?.id);
}

export function useVocabularyInvalidation() {
  const queryClient = useQueryClient();
  return () => Promise.all([
    queryClient.invalidateQueries({ queryKey: ['vocabulary'] }),
    queryClient.invalidateQueries({ queryKey: ['stats'] }),
  ]);
}

export function useVocabularyMap() {
  const userId = useUserId();
  return useQuery({
    queryKey: computed(() => ['vocabulary', 'map', userId.value]),
    queryFn: ({ signal }) =>
      request<VocabularyMapItem[]>('GET', '/vocabulary/map', undefined, { signal }),
    enabled: computed(() => !!userId.value),
    staleTime: 60_000,
  });
}

export function useVocabularyList(filters: Ref<VocabularyFilters>) {
  const userId = useUserId();
  return useQuery({
    queryKey: computed(() => ['vocabulary', 'list', userId.value, filters.value.status, filters.value.search]),
    queryFn: ({ signal }) => {
      const params = new URLSearchParams({ limit: String(VOCABULARY_PAGE_SIZE) });
      if (filters.value.status) params.set('status', String(filters.value.status));
      if (filters.value.search.trim()) params.set('search', filters.value.search.trim());
      return request<VocabularyItem[]>('GET', `/vocabulary?${params}`, undefined, { signal });
    },
    enabled: computed(() => !!userId.value),
    placeholderData: keepPreviousData,
  });
}

export function useReviewQueue() {
  const userId = useUserId();
  return useQuery({
    queryKey: computed(() => ['vocabulary', 'review', userId.value]),
    queryFn: ({ signal }) =>
      request<VocabularyItem[]>('GET', '/vocabulary/review', undefined, { signal }),
    enabled: computed(() => !!userId.value),
    staleTime: 0,
    gcTime: 0,
  });
}

export function useSaveVocabulary() {
  const invalidate = useVocabularyInvalidation();
  return useMutation({
    mutationFn: (payload: VocabularyPayload) =>
      request<VocabularyItem>('POST', '/vocabulary', payload),
    meta: { success: MESSAGES.success.wordSaved },
    onSuccess: invalidate,
  });
}

export function useUpdateVocabulary() {
  const invalidate = useVocabularyInvalidation();
  return useMutation({
    mutationFn: ({ id, ...payload }: VocabularyUpdatePayload & { id: string }) =>
      request<VocabularyItem>('PATCH', `/vocabulary/${id}`, payload),
    onSuccess: invalidate,
  });
}

export function useDeleteVocabulary() {
  const invalidate = useVocabularyInvalidation();
  return useMutation({
    mutationFn: (id: string) => request<void>('DELETE', `/vocabulary/${id}`),
    meta: { success: MESSAGES.success.wordDeleted },
    onSuccess: invalidate,
  });
}

export function useAnswerReview() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ id, correct }: { id: string; correct: boolean }) =>
      request<VocabularyItem>('POST', `/vocabulary/${id}/review`, { correct }),
    onSuccess: () => Promise.all([
      queryClient.invalidateQueries({ queryKey: ['vocabulary', 'map'] }),
      queryClient.invalidateQueries({ queryKey: ['vocabulary', 'list'] }),
      queryClient.invalidateQueries({ queryKey: ['stats'] }),
    ]),
  });
}

export function useMarkKnown() {
  const invalidate = useVocabularyInvalidation();
  return useMutation({
    mutationFn: (terms: string[]) =>
      request<{ created: number }>('POST', '/vocabulary/known', { terms }),
    onSuccess: invalidate,
  });
}
