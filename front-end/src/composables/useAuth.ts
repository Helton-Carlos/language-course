import { useMutation } from '@tanstack/vue-query';
import { request } from '@/composables/useApi';
import type { LoginPayload, RegisterPayload, User } from '@/types/user';

export function useLogin() {
  return useMutation({
    mutationFn: (payload: LoginPayload) => request<User>('POST', '/auth/login', payload),
  });
}

export function useRegister() {
  return useMutation({
    mutationFn: (payload: RegisterPayload) => request<User>('POST', '/auth/register', payload),
  });
}
