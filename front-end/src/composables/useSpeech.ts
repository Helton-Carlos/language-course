const SPEECH_LANGUAGE = 'en-US';

export function useSpeech() {
  const supported = typeof window !== 'undefined' && 'speechSynthesis' in window;

  function speak(text: string, rate = 0.9) {
    if (!supported || !text) return;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = SPEECH_LANGUAGE;
    utterance.rate = rate;
    window.speechSynthesis.speak(utterance);
  }

  return { supported, speak };
}
