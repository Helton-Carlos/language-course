<script lang="ts" setup>
import { computed, ref } from 'vue';
import { useRouter } from 'vue-router';
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import ECButton from '@/components/ECButton/ECButton.vue';
import ECInput from '@/components/ECInput/ECInput.vue';
import { useCreateLesson } from '@/composables/useLessons';
import { countWords } from '@/utils/words';

const MAX_BODY_LENGTH = 60000;

const router = useRouter();
const { mutate: createLesson, isPending } = useCreateLesson();

const title = ref<string>('');
const body = ref<string>('');

const wordCount = computed(() => countWords(body.value));
const canSubmit = computed(
  () => !isPending.value && title.value.trim().length > 0 && wordCount.value > 0,
);

function submit() {
  if (!canSubmit.value) return;
  createLesson(
    { title: title.value.trim().slice(0, 200), body: body.value.trim() },
    {
      onSuccess: (lesson) =>
        router.push({ name: 'dashboard-biblioteca-texto', params: { id: lesson.id } }),
    },
  );
}
</script>

<template>
  <section class="max-w-3xl">
    <ECBackButton :to="{ name: 'dashboard-biblioteca' }" />
    <h1 class="mt-4 text-3xl font-bold">
      Importar texto
    </h1>
    <p class="mt-2 text-quaternary">
      Cole um texto em inglês. Depois de salvo, clique nas palavras para ver a tradução e criar LingQs.
    </p>
    <form class="mt-6 flex flex-col gap-4" @submit.prevent="submit">
      <ECInput
        id="lesson-title"
        v-model="title"
        label="Título"
        placeholder="Ex.: Letra de música, notícia, e-mail"
        required
      />
      <div class="flex flex-col gap-1">
        <label for="lesson-body" class="font-medium text-tertiary">
          Texto
        </label>
        <textarea
          id="lesson-body"
          v-model="body"
          rows="14"
          :maxlength="MAX_BODY_LENGTH"
          required
          placeholder="Cole aqui o texto em inglês..."
          class="w-full rounded-md border-2 border-secondary/30 bg-white px-4 py-2 text-tertiary outline-none transition-colors placeholder:text-quaternary/60 focus:border-secondary focus:ring-4 focus:ring-primary"
        />
        <p class="text-sm text-quaternary">
          {{ wordCount }} palavras · {{ body.length }}/{{ MAX_BODY_LENGTH }} caracteres
        </p>
      </div>
      <div>
        <ECButton type="submit" color="secondary" :disabled="!canSubmit">
          Salvar texto
        </ECButton>
      </div>
    </form>
  </section>
</template>
