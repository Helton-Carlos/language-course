import { useSpeechSynthesis } from '@vueuse/core';
import { ref } from 'vue';

const SPEECH_LANGUAGE = 'en-US';
const DEFAULT_RATE = 0.9;

export function useSpeech() {
  const text = ref<string>('');
  const rate = ref<number>(DEFAULT_RATE);
  const { isSupported, speak: play, stop } = useSpeechSynthesis(text, {
    lang: SPEECH_LANGUAGE,
    rate,
  });

  function speak(value: string, speed: number = DEFAULT_RATE): void {
    if (!value) return;
    stop();
    text.value = value;
    rate.value = speed;
    play();
  }

  return { supported: isSupported, speak, stop };
}