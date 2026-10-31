import { ref } from 'vue';
import { ApiError } from '@/composables/useApi';

export function useFormErrors() {
  const errors = ref<Record<string, string>>({});

  function clear() {
    errors.value = {};
  }

  function setFromApi(error: unknown) {
    if (!(error instanceof ApiError)) {
      errors.value = {};
      return;
    }

    const { _form, ...fields } = error.fieldErrors;
    errors.value = fields;
  }

  return { errors, clear, setFromApi };
}
