import { useMutation, useQueryClient } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import { CURRENT_USER_QUERY_KEY } from '@/composables/useCurrentUser';
import { MESSAGES } from '@/utils/message';
import type { LoginPayload, RegisterPayload, User } from '@/types/user';

export function useLogin() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (payload: LoginPayload) => request<User>('POST', '/auth/login', payload),
    meta: {
      pending: MESSAGES.pending.login,
      success: MESSAGES.success.login,
    },
    onSuccess: (user) => {
      queryClient.setQueryData(CURRENT_USER_QUERY_KEY, user);
    },
  });
}

export function useRegister() {
  return useMutation({
    mutationFn: (payload: RegisterPayload) => request<User>('POST', '/auth/register', payload),
    meta: {
      pending: MESSAGES.pending.register,
      success: MESSAGES.success.register,
    },
  });
}

export function useLogout() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: () => request<void>('POST', '/auth/logout'),
    meta: {
      success: MESSAGES.success.logout,
    },
    onSuccess: () => {
      queryClient.setQueryData(CURRENT_USER_QUERY_KEY, null);
    },
  });
}
