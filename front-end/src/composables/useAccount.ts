import { useMutation, useQueryClient } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import { CURRENT_USER_QUERY_KEY } from '@/composables/useCurrentUser';
import { MESSAGES } from '@/utils/message';

export function useDeleteAccount() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (password: string) => request<void>('DELETE', '/auth/account', { password }),
    meta: {
      pending: MESSAGES.pending.accountDelete,
      success: MESSAGES.success.accountDeleted,
    },
    onSuccess: () => {
      queryClient.setQueryData(CURRENT_USER_QUERY_KEY, null);
    },
  });
}
