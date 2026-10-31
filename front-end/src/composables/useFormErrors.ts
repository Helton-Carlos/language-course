import { ref } from 'vue';
import { ApiError, getErrorMessage } from '@/composables/useApi';

export function useFormErrors() {
  const errors = ref<Record<string, string>>({});
  const formError = ref<string | null>(null);

  function clear() {
    errors.value = {};
    formError.value = null;
  }

  function setFromApi(error: unknown) {
    if (error instanceof ApiError && Object.keys(error.fieldErrors).length > 0) {
      const { _form, ...fields } = error.fieldErrors;
      errors.value = fields;
      formError.value = _form ?? null;
      return;
    }

    errors.value = {};
    formError.value = getErrorMessage(error);
  }

  return { errors, formError, clear, setFromApi };
}
