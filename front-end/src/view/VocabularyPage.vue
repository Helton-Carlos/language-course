<script lang="ts" setup>
import { computed, ref, watch } from 'vue';
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import ECButton from '@/components/ECButton/ECButton.vue';
import ECInput from '@/components/ECInput/ECInput.vue';
import { useSpeech } from '@/composables/useSpeech';
import { toast } from '@/composables/useToast';
import {
  useDeleteVocabulary,
  useSaveVocabulary,
  useUpdateVocabulary,
  useVocabularyList,
} from '@/composables/useVocabulary';
import type { VocabularyFilters, WordStatus } from '@/types/lingq';
import { MESSAGES } from '@/utils/message';
import {
  STATUS_BADGE_CLASSES,
  STATUS_LABELS,
  WORD_STATUSES,
  isValidTerm,
  normalizeTerm,
} from '@/utils/words';

const SEARCH_DELAY = 300;

const statusFilter = ref<WordStatus | null>(null);
const searchInput = ref<string>('');
const search = ref<string>('');
const filters = computed<VocabularyFilters>(() => ({
  status: statusFilter.value,
  search: search.value,
}));

const { data: items, isPending, isError } = useVocabularyList(filters);
const { mutate: updateItem } = useUpdateVocabulary();
const { mutate: deleteItem } = useDeleteVocabulary();
const { mutate: saveItem, isPending: isSaving } = useSaveVocabulary();
const { supported, speak } = useSpeech();

const newTerm = ref<string>('');
const newMeaning = ref<string>('');
const normalizedNewTerm = computed(() => normalizeTerm(newTerm.value));
const canAdd = computed(
  () => !isSaving.value && isValidTerm(normalizedNewTerm.value) && newMeaning.value.trim().length > 0,
);

const editingId = ref<string | null>(null);
const editingMeaning = ref<string>('');

function addItem() {
  if (!canAdd.value) return;
  saveItem(
    { term: normalizedNewTerm.value, meaning: newMeaning.value.trim(), status: 1 },
    {
      onSuccess: () => {
        newTerm.value = '';
        newMeaning.value = '';
      },
    },
  );
}

function startEditing(id: string, meaning: string) {
  editingId.value = id;
  editingMeaning.value = meaning;
}

function finishEditing(id: string, previous: string) {
  const meaning = editingMeaning.value.trim();
  editingId.value = null;
  if (meaning && meaning !== previous) updateItem({ id, meaning });
}

function changeStatus(id: string, event: Event) {
  updateItem({ id, status: Number((event.target as HTMLSelectElement).value) as WordStatus });
}

function confirmDelete(id: string, term: string) {
  toast.confirm(`Remover "${term}" do vocabulário?`, () => deleteItem(id), 'Remover');
}

let searchTimer: ReturnType<typeof setTimeout> | undefined;
watch(searchInput, (value) => {
  clearTimeout(searchTimer);
  searchTimer = setTimeout(() => (search.value = value), SEARCH_DELAY);
});
</script>

<template>
  <section>
    <ECBackButton :to="{ name: 'dashboard' }" />
    <h1 class="mt-4 text-3xl font-bold">
      Vocabulário
    </h1>
    <p class="mt-2 text-quaternary">
      Todas as palavras e frases que você salvou como LingQs.
    </p>

    <form class="mt-6 grid gap-4 rounded-2xl bg-white p-5 shadow-sm md:grid-cols-[1fr_1fr_auto] md:items-end" @submit.prevent="addItem">
      <ECInput
        id="new-term"
        v-model="newTerm"
        label="Palavra ou frase"
        placeholder="Ex.: look forward to"
      />
      <ECInput
        id="new-meaning"
        v-model="newMeaning"
        label="Significado"
        placeholder="Ex.: ansiar por"
      />
      <ECButton type="submit" color="secondary" :disabled="!canAdd">
        Adicionar
      </ECButton>
    </form>

    <div class="mt-6 flex flex-wrap items-center gap-2" role="group" aria-label="Filtrar por nível de conhecimento">
      <button
        type="button"
        :aria-pressed="statusFilter === null"
        :class="[
          'cursor-pointer rounded-md px-3 py-1.5 text-sm font-medium transition-colors',
          statusFilter === null ? 'bg-secondary text-white' : 'bg-white text-tertiary hover:bg-primary',
        ]"
        @click="statusFilter = null"
      >
        Todas
      </button>
      <button
        v-for="status in WORD_STATUSES"
        :key="status"
        type="button"
        :aria-pressed="statusFilter === status"
        :class="[
          'cursor-pointer rounded-md px-3 py-1.5 text-sm font-medium transition',
          STATUS_BADGE_CLASSES[status],
          statusFilter === status ? 'ring-2 ring-secondary' : 'opacity-80 hover:opacity-100',
        ]"
        @click="statusFilter = status"
      >
        {{ STATUS_LABELS[status] }}
      </button>
      <div class="ml-auto w-full sm:w-64">
        <input
          v-model="searchInput"
          type="search"
          aria-label="Buscar no vocabulário"
          placeholder="Buscar palavra ou significado"
          class="w-full rounded-md border-2 border-secondary/30 bg-white px-3 py-1.5 text-tertiary outline-none transition-colors placeholder:text-quaternary/60 focus:border-secondary focus:ring-4 focus:ring-primary"
        >
      </div>
    </div>

    <p v-if="isPending" class="mt-6">
      {{ MESSAGES.pending.vocabularyLoad }}
    </p>
    <p v-else-if="isError" class="mt-6 text-red-700" role="alert">
      {{ MESSAGES.error.vocabularyLoad }}
    </p>
    <div v-else-if="!items?.length" class="mt-6 rounded-2xl bg-white p-6 shadow-sm">
      <p class="font-medium text-tertiary">
        Nenhuma palavra encontrada.
      </p>
      <p class="mt-1 text-quaternary">
        Abra um texto na
        <router-link :to="{ name: 'dashboard-biblioteca' }" class="font-medium text-secondary underline">
          biblioteca
        </router-link>
        e clique nas palavras para criar LingQs.
      </p>
    </div>
    <ul v-else class="mt-6 flex flex-col gap-3">
      <li
        v-for="item in items"
        :key="item.id"
        class="grid gap-3 rounded-2xl bg-white p-4 shadow-sm md:grid-cols-[minmax(0,1fr)_minmax(0,1.2fr)_auto] md:items-center"
      >
        <div class="flex min-w-0 items-center gap-2">
          <p class="break-words text-lg font-bold text-tertiary">
            {{ item.term }}
          </p>
          <button
            v-if="supported"
            type="button"
            class="cursor-pointer rounded-md p-1.5 text-secondary transition-colors hover:bg-gray"
            :aria-label="`Ouvir ${item.term}`"
            @click="speak(item.term)"
          >
            <svg
              viewBox="0 0 24 24"
              fill="currentColor"
              class="h-4 w-4"
              aria-hidden="true"
            >
              <path d="M3 9v6h4l5 5V4L7 9H3Zm11-5.8v2.1a7 7 0 0 1 0 13.4v2.1a9 9 0 0 0 0-17.6Z" />
            </svg>
          </button>
        </div>
        <div class="min-w-0">
          <input
            v-if="editingId === item.id"
            v-model="editingMeaning"
            type="text"
            maxlength="300"
            :aria-label="`Significado de ${item.term}`"
            class="w-full rounded-md border-2 border-secondary/30 bg-white px-3 py-1 text-tertiary outline-none focus:border-secondary focus:ring-4 focus:ring-primary"
            autofocus
            @blur="finishEditing(item.id, item.meaning)"
            @keydown.enter.prevent="finishEditing(item.id, item.meaning)"
            @keydown.esc.prevent="editingId = null"
          >
          <button
            v-else
            type="button"
            class="w-full cursor-text break-words rounded-md px-1 py-1 text-left text-quaternary hover:bg-gray"
            :title="'Clique para editar o significado'"
            @click="startEditing(item.id, item.meaning)"
          >
            {{ item.meaning || 'Adicionar significado' }}
          </button>
        </div>
        <div class="flex items-center gap-2">
          <select
            :value="item.status"
            :aria-label="`Nível de ${item.term}`"
            :class="['cursor-pointer rounded-md px-2 py-1.5 text-sm font-medium', STATUS_BADGE_CLASSES[item.status]]"
            @change="changeStatus(item.id, $event)"
          >
            <option v-for="status in WORD_STATUSES" :key="status" :value="status">
              {{ STATUS_LABELS[status] }}
            </option>
          </select>
          <button
            type="button"
            class="cursor-pointer rounded-md p-1.5 text-red-700 transition-colors hover:bg-gray"
            :aria-label="`Remover ${item.term}`"
            @click="confirmDelete(item.id, item.term)"
          >
            <svg
              viewBox="0 0 24 24"
              fill="currentColor"
              class="h-5 w-5"
              aria-hidden="true"
            >
              <path d="M6 19a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V7H6v12ZM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4Z" />
            </svg>
          </button>
        </div>
      </li>
    </ul>
  </section>
</template>
