import { useMutation, useQueryClient } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import { CURRENT_USER_QUERY_KEY } from '@/composables/useCurrentUser';
import { MESSAGES } from '@/utils/message';
import type { ProfilePayload, User } from '@/types/user';

export function useSaveProfile() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (payload: ProfilePayload) => request<User>('PUT', '/users/me/profile', payload),
    meta: {
      pending: MESSAGES.pending.profile,
      success: MESSAGES.success.profile,
    },
    onSuccess: (user) => {
      queryClient.setQueryData(CURRENT_USER_QUERY_KEY, user);
    },
  });
}
