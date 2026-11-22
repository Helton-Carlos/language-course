<script setup lang="ts">
import { Volume2, X } from 'lucide-vue-next';
import { computed, ref, watch } from 'vue';
import ECButton from '@/components/ECButton/ECButton.vue';
import type { ECWordPanel } from '@/components/ECWordPanel/Type';
import { useDictionary } from '@/composables/useDictionary';
import { useSpeech } from '@/composables/useSpeech';
import { useSaveVocabulary, useVocabularyMap } from '@/composables/useVocabulary';
import type { WordStatus } from '@/types/study';
import {
  KNOWN_STATUS,
  STATUS_BADGE_CLASSES,
  STATUS_LABELS,
  WORD_STATUSES,
} from '@/utils/words';

const { term, context } = defineProps<ECWordPanel>();

const emit = defineEmits<{
  (e: 'close'): void;
}>();

const termRef = computed(() => term);
const { data: vocabulary } = useVocabularyMap();
const { data: entry, isPending: isLookingUp } = useDictionary(termRef);
const { mutate: save, isPending: isSaving } = useSaveVocabulary();
const { supported, speak } = useSpeech();

const existing = computed(() => vocabulary.value?.find((item) => item.term === term));
const meaning = ref<string>('');
const status = ref<WordStatus>(1);
const meaningTouched = ref<boolean>(false);

const canSave = computed(
  () => !isSaving.value && (status.value === KNOWN_STATUS || meaning.value.trim().length > 0),
);

function pickSuggestion(suggestion: string) {
  meaning.value = suggestion;
  meaningTouched.value = true;
}

function submit() {
  if (!canSave.value) return;
  save({
    term,
    meaning: meaning.value.trim(),
    context: context?.trim() || undefined,
    status: status.value,
  });
}

function markKnown() {
  status.value = KNOWN_STATUS;
  submit();
}

watch(
  () => term,
  () => {
    meaning.value = existing.value?.meaning ?? '';
    status.value = existing.value?.status ?? 1;
    meaningTouched.value = false;
  },
  { immediate: true },
);

watch(
  () => entry.value?.translation,
  (translation) => {
    if (translation && !meaningTouched.value && !meaning.value) meaning.value = translation;
  },
  { immediate: true },
);
</script>

<template>
  <section class="rounded-2xl bg-white p-5 shadow-sm" aria-live="polite">
    <header class="flex items-start justify-between gap-3">
      <div class="min-w-0">
        <h2 class="break-words text-2xl font-bold text-tertiary">
          {{ term }}
        </h2>
        <p v-if="entry?.phonetic" class="text-quaternary">
          {{ entry.phonetic }}
        </p>
      </div>
      <div class="flex shrink-0 items-center gap-1">
        <button
          v-if="supported"
          type="button"
          class="cursor-pointer rounded-md p-2 text-secondary transition-colors hover:bg-gray"
          aria-label="Ouvir pronúncia"
          @click="speak(term)"
        >
          <Volume2 class="h-5 w-5" aria-hidden="true" />
        </button>
        <button
          type="button"
          class="cursor-pointer rounded-md p-2 text-quaternary transition-colors hover:bg-gray"
          aria-label="Fechar painel"
          @click="emit('close')"
        >
          <X class="h-5 w-5" aria-hidden="true" />
        </button>
      </div>
    </header>

    <p v-if="existing" class="mt-2">
      <span :class="['rounded px-2 py-0.5 font-medium', STATUS_BADGE_CLASSES[existing.status]]">
        {{ STATUS_LABELS[existing.status] }}
      </span>
    </p>

    <p v-if="entry?.definition" class="mt-3 text-quaternary">
      {{ entry.definition }}
    </p>

    <div class="mt-4">
      <label for="word-meaning" class="font-medium text-tertiary">
        Significado
      </label>
      <input
        id="word-meaning"
        v-model="meaning"
        type="text"
        maxlength="300"
        autocomplete="off"
        :placeholder="isLookingUp ? 'Buscando tradução...' : 'Escreva o significado'"
        class="mt-1 w-full rounded-md border-2 border-secondary/30 bg-white px-3 py-2 text-tertiary outline-none transition-colors placeholder:text-quaternary/60 focus:border-secondary focus:ring-4 focus:ring-primary"
        @input="meaningTouched = true"
        @keydown.enter.prevent="submit"
      >
      <ul v-if="entry?.suggestions.length" class="mt-2 flex flex-wrap gap-2">
        <li v-for="suggestion in entry.suggestions" :key="suggestion">
          <button
            type="button"
            class="cursor-pointer rounded-full bg-gray px-3 py-1 text-tertiary transition-colors hover:bg-primary"
            @click="pickSuggestion(suggestion)"
          >
            {{ suggestion }}
          </button>
        </li>
      </ul>
    </div>

    <p v-if="context" class="mt-4 rounded-md bg-gray px-3 py-2 italic text-quaternary">
      {{ context }}
    </p>

    <fieldset class="mt-4">
      <legend class="font-medium text-tertiary">
        Nível de conhecimento
      </legend>
      <div class="mt-2 flex flex-wrap gap-2">
        <button
          v-for="option in WORD_STATUSES"
          :key="option"
          type="button"
          :aria-pressed="status === option"
          :class="[
            'cursor-pointer rounded-md px-3 py-1.5 font-medium transition',
            STATUS_BADGE_CLASSES[option],
            status === option ? 'ring-2 ring-secondary' : 'opacity-70 hover:opacity-100',
          ]"
          @click="status = option"
        >
          {{ STATUS_LABELS[option] }}
        </button>
      </div>
    </fieldset>

    <div class="mt-5 flex flex-wrap gap-3">
      <ECButton color="secondary" :disabled="!canSave" @on-click="submit">
        Salvar
      </ECButton>
      <ECButton color="border" :disabled="isSaving" @on-click="markKnown">
        Já sei
      </ECButton>
    </div>
  </section>
</template>
