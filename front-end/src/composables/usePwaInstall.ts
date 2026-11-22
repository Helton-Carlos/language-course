import { useEventListener } from '@vueuse/core';
import { computed, ref } from 'vue';

interface BeforeInstallPromptEvent extends Event {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: 'accepted' | 'dismissed' }>;
}

const installPrompt = ref<BeforeInstallPromptEvent | null>(null);

export function usePwaInstall() {
  const canInstall = computed<boolean>(() => installPrompt.value !== null);

  useEventListener(window, 'beforeinstallprompt', (event: Event) => {
    event.preventDefault();
    installPrompt.value = event as BeforeInstallPromptEvent;
  });

  useEventListener(window, 'appinstalled', () => {
    installPrompt.value = null;
  });

  async function install(): Promise<void> {
    const prompt = installPrompt.value;
    if (!prompt) return;
    await prompt.prompt();
    await prompt.userChoice;
    installPrompt.value = null;
  }

  return { canInstall, install };
}