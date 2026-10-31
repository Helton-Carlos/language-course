import { computed, ref } from 'vue';

const apiUrl = import.meta.env.VITE_API as string;

type Method = 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE';

export class ApiError extends Error {
  readonly status: number;
  readonly fieldErrors: Record<string, string>;

  constructor(status: number, message: string, fieldErrors: Record<string, string> = {}) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
    this.fieldErrors = fieldErrors;
  }
}

async function toApiError(response: Response, fallback: string): Promise<ApiError> {
  let detail: unknown;

  try {
    const data: unknown = await response.json();
    detail = (data as { detail?: unknown } | null)?.detail;
  } catch {
    detail = undefined;
  }

  if (typeof detail === 'string') {
    return new ApiError(response.status, detail);
  }

  if (Array.isArray(detail)) {
    const fieldErrors: Record<string, string> = {};

    for (const item of detail as { loc?: unknown[]; msg?: string }[]) {
      const field = (item.loc ?? []).slice(1).join('.') || '_form';
      const message = (item.msg ?? 'Valor inválido').replace(/^Value error, /, '');
      fieldErrors[field] ??= message;
    }

    return new ApiError(response.status, 'Verifique os dados informados.', fieldErrors);
  }

  return new ApiError(response.status, fallback);
}

export function getErrorMessage(error: unknown): string {
  if (error instanceof ApiError) {
    return error.message;
  }

  if (error instanceof TypeError) {
    return 'Não foi possível conectar ao servidor.';
  }

  return 'Erro inesperado. Tente novamente.';
}

export async function request<T>(
  method: Method,
  path: string,
  body?: unknown,
  init?: RequestInit,
): Promise<T> {
  const hasBody = body !== undefined;

  const response = await fetch(`${apiUrl}${path}`, {
    credentials: 'include',
    ...init,
    method,
    headers: {
      ...(hasBody ? { 'Content-Type': 'application/json' } : {}),
      ...init?.headers,
    },
    body: hasBody ? JSON.stringify(body) : undefined,
  });

  if (!response.ok) {
    throw await toApiError(response, `Erro ${response.status} em ${method} ${path}`);
  }

  if (response.status === 204) {
    return undefined as T;
  }

  return (await response.json()) as T;
}

export function useApi() {
  const pending = ref(0);
  const error = ref<string | null>(null);
  const loading = computed(() => pending.value > 0);

  async function run<T>(fn: () => Promise<T>): Promise<T> {
    pending.value++;
    error.value = null;

    try {
      return await fn();
    } catch (e) {
      error.value = e instanceof Error ? e.message : 'Erro desconhecido';
      throw e;
    } finally {
      pending.value--;
    }
  }

  const get = <T>(path: string, init?: RequestInit) =>
    run(() => request<T>('GET', path, undefined, init));

  const post = <T>(path: string, body?: unknown, init?: RequestInit) =>
    run(() => request<T>('POST', path, body, init));

  const update = <T>(path: string, body?: unknown, init?: RequestInit) =>
    run(() => request<T>('PUT', path, body, init));

  const patch = <T>(path: string, body?: unknown, init?: RequestInit) =>
    run(() => request<T>('PATCH', path, body, init));

  const remove = <T = void>(path: string, init?: RequestInit) =>
    run(() => request<T>('DELETE', path, undefined, init));

  return { loading, error, get, post, update, patch, delete: remove };
}
