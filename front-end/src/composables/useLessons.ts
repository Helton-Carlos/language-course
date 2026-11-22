import { computed, type Ref } from 'vue';
import { useMutation, useQuery, useQueryClient } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import { useCurrentUser } from '@/composables/useCurrentUser';
import { MESSAGES } from '@/utils/message';
import type { Lesson, LessonPayload, LessonSummary } from '@/types/lingq';

export function useLessons() {
  const { data: user } = useCurrentUser();
  return useQuery({
    queryKey: computed(() => ['lessons', user.value?.id]),
    queryFn: ({ signal }) => request<LessonSummary[]>('GET', '/lessons', undefined, { signal }),
    enabled: computed(() => !!user.value),
  });
}

export function useLesson(id: Ref<string>) {
  const { data: user } = useCurrentUser();
  return useQuery({
    queryKey: computed(() => ['lessons', user.value?.id, id.value]),
    queryFn: ({ signal }) => request<Lesson>('GET', `/lessons/${id.value}`, undefined, { signal }),
    enabled: computed(() => !!user.value && !!id.value),
    staleTime: 10 * 60_000,
  });
}

export function useCreateLesson() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (payload: LessonPayload) => request<Lesson>('POST', '/lessons', payload),
    meta: {
      pending: MESSAGES.pending.lessonSave,
      success: MESSAGES.success.lessonSaved,
    },
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['lessons'] }),
  });
}

export function useDeleteLesson() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (id: string) => request<void>('DELETE', `/lessons/${id}`),
    meta: { success: MESSAGES.success.lessonDeleted },
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['lessons'] }),
  });
}
