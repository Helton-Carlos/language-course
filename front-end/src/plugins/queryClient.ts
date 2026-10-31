import { MutationCache, QueryCache, QueryClient } from '@tanstack/vue-query';
import { ApiError, getErrorMessage } from '@/composables/useApi';
import { toast } from '@/composables/useToast';

declare module '@tanstack/query-core' {
  interface Register {
    mutationMeta: {
      pending?: string;
      success?: string;
    };
  }
}

const PENDING_DELAY = 400;

interface PendingEntry {
  timer?: ReturnType<typeof setTimeout>;
  toastId?: number;
}

const pendingToasts = new Map<number, PendingEntry>();

function startPending(mutationId: number, message?: string) {
  if (!message) return;

  const entry: PendingEntry = {};
  entry.timer = setTimeout(() => {
    entry.toastId = toast.pending(message);
  }, PENDING_DELAY);

  pendingToasts.set(mutationId, entry);
}

function stopPending(mutationId: number) {
  const entry = pendingToasts.get(mutationId);
  if (!entry) return;

  clearTimeout(entry.timer);
  if (entry.toastId !== undefined) toast.dismiss(entry.toastId);
  pendingToasts.delete(mutationId);
}

function notifyApiError(error: unknown) {
  if (error instanceof ApiError) {
    const { _form, ...fields } = error.fieldErrors;

    if (Object.keys(fields).length > 0) return;
    if (_form) {
      toast.error(_form);
      return;
    }
  }

  toast.error(getErrorMessage(error));
}

export const queryClient = new QueryClient({
  queryCache: new QueryCache({ onError: notifyApiError }),
  mutationCache: new MutationCache({
    onMutate: (_variables, mutation) => {
      startPending(mutation.mutationId, mutation.meta?.pending);
    },
    onSuccess: (_data, _variables, _context, mutation) => {
      stopPending(mutation.mutationId);
      if (mutation.meta?.success) toast.success(mutation.meta.success);
    },
    onError: (error, _variables, _context, mutation) => {
      stopPending(mutation.mutationId);
      notifyApiError(error);
    },
  }),
});
