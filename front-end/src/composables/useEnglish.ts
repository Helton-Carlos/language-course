import { computed } from 'vue';
import { useLanguages } from '@/composables/useLanguages';

export const ENGLISH_CODE = 'en-US';

export function useEnglish() {
  const { languages, isPending, isError } = useLanguages();

  const english = computed(() => languages.value.find((item) => item.code === ENGLISH_CODE));

  return { english, isPending, isError };
}
