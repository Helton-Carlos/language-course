import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useApi } from '@/composables/useApi';
import type { Language } from '@/types/language'

export const languagesStore = defineStore('languages', () => {
  const api = useApi();
  const languages = ref<Language[]>([]);

  async function fetchLanguages(): Promise<void> {
    try {
      languages.value = await api.get<Language[]>('/languages');
    } catch (e) {
      console.error(e)
     }
  }

  return {
    languages,
    loading: api.loading,
    error: api.error,
    fetchLanguages,
  };
});
