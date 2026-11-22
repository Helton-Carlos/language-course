import { readonly, ref } from 'vue';

const isOpen = ref<boolean>(false);

function open(): void {
  isOpen.value = true;
}

function close(): void {
  isOpen.value = false;
}

function toggle(): void {
  isOpen.value = !isOpen.value;
}

export function useMobileMenu() {
  return { isOpen: readonly(isOpen), open, close, toggle };
}