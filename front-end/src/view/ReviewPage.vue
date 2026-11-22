<script lang="ts" setup>
import { Check, Eye, RotateCcw, Volume2, X } from 'lucide-vue-next';
import { onKeyStroke } from '@vueuse/core';
import { computed, ref, watch } from 'vue';
import ECPageHeader from '@/components/ECPageHeader/ECPageHeader.vue';
import ECButton from '@/components/ECButton/ECButton.vue';
import { useSpeech } from '@/composables/useSpeech';
import { useAnswerReview, useReviewQueue } from '@/composables/useVocabulary';
import type { VocabularyItem } from '@/types/study';
import { MESSAGES } from '@/utils/message';
import { STATUS_BADGE_CLASSES, STATUS_LABELS } from '@/utils/words';

const { data, isPending, isError, refetch, isRefetching } = useReviewQueue();
const { mutate: answer, isPending: isAnswering } = useAnswerReview();
const { supported, speak } = useSpeech();

const queue = ref<VocabularyItem[]>([]);
const position = ref<number>(0);
const revealed = ref<boolean>(false);
const correctCount = ref<number>(0);
const loaded = ref<boolean>(false);

const current = computed(() => queue.value[position.value] ?? null);
const finished = computed(() => loaded.value && !current.value);

function reveal() {
  revealed.value = true;
}

function submit(correct: boolean) {
  const item = current.value;
  if (!item || isAnswering.value) return;
  answer(
    { id: item.id, correct },
    {
      onSuccess: () => {
        if (correct) correctCount.value++;
        position.value++;
        revealed.value = false;
      },
    },
  );
}

function isTypingTarget(event: KeyboardEvent): boolean {
  return event.target instanceof HTMLElement && !!event.target.closest('button, a, input, textarea, select');
}

onKeyStroke([' ', 'Enter'], (event) => {
  if (revealed.value || !current.value || isTypingTarget(event)) return;
  event.preventDefault();
  reveal();
});

onKeyStroke('ArrowLeft', () => {
  if (revealed.value) submit(false);
});

onKeyStroke('ArrowRight', () => {
  if (revealed.value) submit(true);
});

async function reload() {
  loaded.value = false;
  await refetch();
  if (data.value) {
    queue.value = [...data.value];
    position.value = 0;
    correctCount.value = 0;
    revealed.value = false;
  }
  loaded.value = true;
}

watch(
  data,
  (items) => {
    if (!items || loaded.value) return;
    queue.value = [...items];
    position.value = 0;
    correctCount.value = 0;
    revealed.value = false;
    loaded.value = true;
  },
  { immediate: true },
);
</script>

<template>
  <section class="max-w-2xl">
    <ECPageHeader
      :back-to="{ name: 'dashboard' }"
      title="Revisar"
    >
      <template #description>
        Tente lembrar o significado antes de virar o cartão. Acertar sobe o nível da palavra, errar desce.
        Atalhos: espaço mostra a resposta, seta para a esquerda marca erro e seta para a direita marca acerto.
      </template>
    </ECPageHeader>

    <p v-if="isPending" class="mt-6">
      {{ MESSAGES.pending.reviewLoad }}
    </p>
    <p v-else-if="isError" class="mt-6 text-red-700" role="alert">
      {{ MESSAGES.error.reviewLoad }}
    </p>

    <div v-else-if="finished" class="mt-6 rounded-2xl bg-white p-6 shadow-sm">
      <p class="text-xl font-bold text-tertiary">
        {{ queue.length ? 'Revisão concluída' : 'Nada para revisar agora' }}
      </p>
      <p class="mt-1 text-quaternary">
        <template v-if="queue.length">
          Você acertou {{ correctCount }} de {{ queue.length }} cartões.
        </template>
        <template v-else>
          Salve novas palavras lendo textos ou volte mais tarde, quando houver cartões agendados.
        </template>
      </p>
      <div class="mt-5 flex flex-wrap gap-3">
        <ECButton color="secondary" :disabled="isRefetching" @on-click="reload">
          <RotateCcw class="mr-1 inline h-5 w-5 align-text-bottom" aria-hidden="true" />
          Buscar mais cartões
        </ECButton>
        <router-link :to="{ name: 'dashboard-biblioteca' }" class="btn btn-border">
          Ir para a biblioteca
        </router-link>
      </div>
    </div>

    <div v-else-if="current" class="mt-6">
      <div class="flex items-center justify-between text-quaternary">
        <span>Cartão {{ position + 1 }} de {{ queue.length }}</span>
        <span :class="['rounded px-2 py-0.5 font-medium', STATUS_BADGE_CLASSES[current.status]]">
          {{ STATUS_LABELS[current.status] }}
        </span>
      </div>
      <div
        class="mt-2 h-2 overflow-hidden rounded-full bg-white"
        role="progressbar"
        :aria-valuenow="position"
        :aria-valuemax="queue.length"
        aria-valuemin="0"
      >
        <div class="h-full bg-primary transition-all" :style="{ width: `${(position / queue.length) * 100}%` }" />
      </div>

      <div class="mt-4 rounded-2xl bg-white p-8 text-center shadow-sm">
        <p class="break-words text-4xl font-bold text-tertiary">
          {{ current.term }}
        </p>
        <button
          v-if="supported"
          type="button"
          class="mt-3 cursor-pointer font-medium text-secondary hover:underline"
          @click="speak(current.term)"
        >
          <Volume2 class="mr-1 inline h-5 w-5 align-text-bottom" aria-hidden="true" />
          Ouvir pronúncia
        </button>

        <div v-if="revealed" class="mt-6 border-t border-tertiary/15 pt-6">
          <p class="text-2xl text-tertiary">
            {{ current.meaning }}
          </p>
          <p v-if="current.context" class="mt-4 rounded-md bg-gray px-3 py-2 italic text-quaternary">
            {{ current.context }}
          </p>
        </div>
      </div>

      <div class="mt-6 flex flex-wrap justify-center gap-3">
        <ECButton v-if="!revealed" color="secondary" @on-click="reveal">
          <Eye class="mr-1 inline h-5 w-5 align-text-bottom" aria-hidden="true" />
          Mostrar resposta
        </ECButton>
        <template v-else>
          <ECButton color="border" :disabled="isAnswering" @on-click="submit(false)">
            <X class="mr-1 inline h-5 w-5 align-text-bottom" aria-hidden="true" />
            Errei
          </ECButton>
          <ECButton color="primary" :disabled="isAnswering" @on-click="submit(true)">
            <Check class="mr-1 inline h-5 w-5 align-text-bottom" aria-hidden="true" />
            Acertei
          </ECButton>
        </template>
      </div>
    </div>
  </section>
</template>
