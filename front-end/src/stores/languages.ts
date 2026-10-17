import { defineStore } from 'pinia';
import { ref } from 'vue';

export interface Language {
  code: string;
  name: string;
  prefix: string;
}

const API_URL = import.meta.env.VITE_API;

export const languagesStore = defineStore('languages', () => {
  const languages = ref<Language[]>([]);
  const loading = ref<boolean>(false);
  const error = ref<string | null>(null);

  async function fetchLanguages(): Promise<void> {
    loading.value = true;
    error.value = null;

    try {
      const response = await fetch(`${API_URL}/languages`);

      if (!response.ok) {
        throw new Error(`Erro ${response.status} ao buscar idiomas`);
      }

      languages.value = (await response.json()) as Language[];
    } catch (e) {
      error.value = e instanceof Error ? e.message : 'Erro desconhecido';
    } finally {
      loading.value = false;
    }
  }

  return { languages, loading, error, fetchLanguages };
});
