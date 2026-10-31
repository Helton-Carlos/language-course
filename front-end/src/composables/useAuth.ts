import { useMutation } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import { MESSAGES } from '@/utils/message';
import type { LoginPayload, RegisterPayload, User } from '@/types/user';

export function useLogin() {
  return useMutation({
    mutationFn: (payload: LoginPayload) => request<User>('POST', '/auth/login', payload),
    meta: {
      pending: MESSAGES.pending.login,
      success: MESSAGES.success.login,
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
