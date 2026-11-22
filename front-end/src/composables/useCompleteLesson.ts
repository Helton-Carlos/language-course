import { computed, type Ref } from 'vue';
import { useMarkKnown, useVocabularyMap } from '@/composables/useVocabulary';
import { useRecordReading } from '@/composables/useStats';
import { toast } from '@/composables/useToast';
import { MESSAGES } from '@/utils/message';
import { countWords, extractTerms, isValidTerm } from '@/utils/words';

const BULK_CHUNK_SIZE = 3000;

export function useCompleteLesson(body: Ref<string>) {
  const { data: vocabulary } = useVocabularyMap();
  const markKnown = useMarkKnown();
  const recordReading = useRecordReading();

  const unknownTerms = computed(() => {
    const saved = new Set((vocabulary.value ?? []).map((item) => item.term));
    return extractTerms(body.value).filter((term) => isValidTerm(term) && !saved.has(term));
  });

  const isCompleting = computed(() => markKnown.isPending.value || recordReading.isPending.value);

  async function complete() {
    const terms = unknownTerms.value;
    try {
      for (let start = 0; start < terms.length; start += BULK_CHUNK_SIZE) {
        await markKnown.mutateAsync(terms.slice(start, start + BULK_CHUNK_SIZE));
      }
      await recordReading.mutateAsync(Math.max(1, countWords(body.value)));
      toast.success(MESSAGES.success.lessonCompleted);
    } catch {
      return;
    }
  }

  return { unknownTerms, isCompleting, complete };
}
