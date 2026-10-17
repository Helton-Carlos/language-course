import { computed, ref } from 'vue';

const apiUrl = import.meta.env.VITE_API as string;

type Method = 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE';

async function request<T>(
  method: Method,
  path: string,
  body?: unknown,
  init?: RequestInit,
): Promise<T> {
  const hasBody = body !== undefined;

  const response = await fetch(`${apiUrl}${path}`, {
    ...init,
    method,
    headers: {
      ...(hasBody ? { 'Content-Type': 'application/json' } : {}),
      ...init?.headers,
    },
    body: hasBody ? JSON.stringify(body) : undefined,
  });

  console.log("apiUrl")
  console.log(response)
  if (!response.ok) {
    throw new Error(`Erro ${response.status} em ${method} ${path}`);
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
