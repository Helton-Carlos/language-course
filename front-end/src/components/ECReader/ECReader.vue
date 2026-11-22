<script setup lang="ts">
import { computed, ref } from 'vue';
import ECWordPanel from '@/components/ECWordPanel/ECWordPanel.vue';
import type { ECReader } from '@/components/ECReader/Type';
import { useSpeech } from '@/composables/useSpeech';
import { useVocabularyMap } from '@/composables/useVocabulary';
import {
  MAX_PHRASE_WORDS,
  STATUS_LABELS,
  STATUS_WORD_CLASSES,
  UNKNOWN_WORD_CLASS,
  WORD_STATUSES,
  countWords,
  isValidTerm,
  normalizeTerm,
  splitParagraphs,
  tokenizeLine,
} from '@/utils/words';

const { body } = defineProps<ECReader>();

interface Selection {
  term: string;
  context: string;
}

const MAX_CONTEXT_LENGTH = 1000;

const { data: vocabulary } = useVocabularyMap();
const { supported, speak } = useSpeech();

const itemsByTerm = computed(() => new Map((vocabulary.value ?? []).map((item) => [item.term, item])));
const paragraphs = computed(() =>
  splitParagraphs(body).map((text) => ({ text, tokens: tokenizeLine(text) })),
);
const selection = ref<Selection | null>(null);
const container = ref<HTMLElement | null>(null);

function wordClass(term: string): string {
  const item = itemsByTerm.value.get(term);
  return item ? STATUS_WORD_CLASSES[item.status] : UNKNOWN_WORD_CLASS;
}

function sentenceFor(paragraph: string, term: string): string {
  const sentences = paragraph.split(/(?<=[.!?])\s+/);
  const found = sentences.find((sentence) => normalizeTerm(sentence).includes(term));
  return (found ?? paragraph).slice(0, MAX_CONTEXT_LENGTH);
}

function selectWord(paragraphIndex: number, term: string) {
  if (window.getSelection()?.toString().trim()) return;
  selection.value = { term, context: sentenceFor(paragraphs.value[paragraphIndex]!.text, term) };
}

function selectPhrase() {
  const current = window.getSelection();
  if (!current || current.isCollapsed || !container.value) return;
  const anchor = current.anchorNode?.parentElement;
  if (!anchor || !container.value.contains(anchor)) return;
  const term = normalizeTerm(current.toString());
  const words = countWords(term);
  if (words < 2 || words > MAX_PHRASE_WORDS || !isValidTerm(term)) return;
  const paragraphIndex = Number(anchor.closest<HTMLElement>('[data-paragraph]')?.dataset.paragraph ?? 0);
  selection.value = { term, context: sentenceFor(paragraphs.value[paragraphIndex]?.text ?? '', term) };
}

function readAloud() {
  speak(body, 0.85);
}
</script>

<template>
  <div class="grid gap-6 lg:grid-cols-[minmax(0,1fr)_22rem]">
    <div>
      <div class="flex flex-wrap items-center gap-x-4 gap-y-2 text-sm text-quaternary">
        <span v-for="status in WORD_STATUSES.slice(0, 4)" :key="status" class="inline-flex items-center gap-1.5">
          <span :class="['inline-block h-3 w-5 rounded-sm', STATUS_WORD_CLASSES[status]]" />
          {{ STATUS_LABELS[status] }}
        </span>
        <span class="inline-flex items-center gap-1.5">
          <span :class="['inline-block h-3 w-5 rounded-sm', UNKNOWN_WORD_CLASS]" />
          Desconhecida
        </span>
        <button
          v-if="supported"
          type="button"
          class="ml-auto cursor-pointer font-medium text-secondary hover:underline"
          @click="readAloud"
        >
          Ouvir texto
        </button>
      </div>

      <div
        ref="container"
        class="mt-4 rounded-2xl bg-white p-6 text-xl leading-loose shadow-sm"
        @mouseup="selectPhrase"
      >
        <p
          v-for="(paragraph, paragraphIndex) in paragraphs"
          :key="paragraphIndex"
          :data-paragraph="paragraphIndex"
          class="mb-4 last:mb-0"
        >
          <template v-for="(token, tokenIndex) in paragraph.tokens" :key="tokenIndex">
            <span
              v-if="token.kind === 'word'"
              role="button"
              tabindex="0"
              :class="[
                'cursor-pointer rounded px-0.5 transition-shadow hover:ring-2 hover:ring-secondary/40 focus-visible:outline-2 focus-visible:outline-secondary',
                wordClass(token.term),
                selection?.term === token.term ? 'ring-2 ring-secondary' : '',
              ]"
              @click="selectWord(paragraphIndex, token.term)"
              @keydown.enter.prevent="selectWord(paragraphIndex, token.term)"
              @keydown.space.prevent="selectWord(paragraphIndex, token.term)"
            >{{ token.text }}</span>
            <template v-else>{{ token.text }}</template>
          </template>
        </p>
      </div>
      <p class="mt-3 text-sm text-quaternary">
        Clique em uma palavra ou selecione um trecho de até {{ MAX_PHRASE_WORDS }} palavras para criar um LingQ.
      </p>
    </div>

    <aside class="lg:sticky lg:top-6 lg:self-start">
      <ECWordPanel
        v-if="selection"
        :key="selection.term"
        :term="selection.term"
        :context="selection.context"
        @close="selection = null"
      />
      <div v-else class="rounded-2xl bg-white p-5 text-quaternary shadow-sm">
        <p class="font-medium text-tertiary">
          Painel de palavras
        </p>
        <p class="mt-1">
          Escolha uma palavra do texto para ver a tradução, ouvir a pronúncia e salvar no seu vocabulário.
        </p>
      </div>
    </aside>
  </div>
</template>
