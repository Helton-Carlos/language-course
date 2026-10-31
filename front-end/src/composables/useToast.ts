import { readonly, ref } from 'vue';

export type ToastType = 'error' | 'success' | 'warning' | 'info';

export interface Toast {
  id: number;
  type: ToastType;
  message: string;
}

const DEFAULT_DURATION = 5000;
const MAX_TOASTS = 4;

const toasts = ref<Toast[]>([]);
let nextId = 0;

function dismiss(id: number) {
  toasts.value = toasts.value.filter((toast) => toast.id !== id);
}

function show(message: string, type: ToastType = 'info', duration = DEFAULT_DURATION): number {
  const existing = toasts.value.find(
    (toast) => toast.type === type && toast.message === message,
  );
  if (existing) return existing.id;

  const id = nextId++;
  toasts.value = [...toasts.value, { id, type, message }].slice(-MAX_TOASTS);

  if (duration > 0) {
    setTimeout(() => dismiss(id), duration);
  }

  return id;
}

export const toast = {
  show,
  dismiss,
  error: (message: string, duration?: number) => show(message, 'error', duration),
  success: (message: string, duration?: number) => show(message, 'success', duration),
  info: (message: string, duration?: number) => show(message, 'info', duration),
  pending: (message: string) => show(message, 'warning', 0),
};

export function useToast() {
  return { toasts: readonly(toasts), ...toast };
}
