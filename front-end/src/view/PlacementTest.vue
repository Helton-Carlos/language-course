<script lang="ts" setup>
import { computed, reactive, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import ECButton from '@/components/ECButton/ECButton.vue';
import { useLanguages } from '@/composables/useLanguages';
import { usePlacementQuestions, useSubmitPlacement } from '@/composables/usePlacement';
import { useSaveProfile } from '@/composables/useProfile';
import { LEVELS, type Level } from '@/utils/levels';
import { MESSAGES } from '@/utils/message';

const route = useRoute();
const router = useRouter();

const languageId = computed(() => String(route.params.id));
const { languages } = useLanguages();
const language = computed(() => languages.value.find((item) => item.id === languageId.value));

const level = ref<Level>(LEVELS[0]);
const finalLevel = ref<Level | null>(null);
const answers = reactive<Record<string, number>>({});

const { data: test, isPending, isError } = usePlacementQuestions(languageId, level);
const { mutate: submit, isPending: isSubmitting } = useSubmitPlacement();
const { mutate: saveProfile, isPending: isSaving } = useSaveProfile();

const step = computed(() => LEVELS.indexOf(level.value) + 1);
const progress = computed(() => Math.round(((step.value - 1) / LEVELS.length) * 100));
const canSubmit = computed(
  () => !!test.value && test.value.questions.every((question) => answers[question.id] !== undefined),
);

function clearAnswers() {
  Object.keys(answers).forEach((key) => delete answers[key]);
}

function onSubmit() {
  if (!canSubmit.value) return;

  submit(
    {
      languageId: languageId.value,
      level: level.value,
      answers: Object.entries(answers).map(([question_id, option_index]) => ({
        question_id,
        option_index,
      })),
    },
    {
      onSuccess: (result) => {
        if (result.result_level) {
          finalLevel.value = result.result_level;
          return;
        }

        if (result.next_level) {
          clearAnswers();
          level.value = result.next_level;
        }
      },
    },
  );
}

function confirm() {
  if (!finalLevel.value) return;

  saveProfile(
    { language_id: languageId.value, level: finalLevel.value },
    { onSuccess: () => router.push({ name: 'dashboard' }) },
  );
}

function chooseAnotherLevel() {
  router.push({
    name: 'escolher-nivel',
    params: { id: languageId.value },
    query: finalLevel.value ? { level: finalLevel.value } : {},
  });
}

function restart() {
  clearAnswers();
  finalLevel.value = null;
  level.value = LEVELS[0];
}
</script>

<template>
  <div class="container my-8 max-w-3xl lg:my-16">
    <router-link
      class="text-quaternary underline"
      :to="{ name: 'escolher-nivel', params: { id: languageId } }"
    >
      Voltar
    </router-link>

    <h1 class="mt-4 text-3xl font-bold lg:text-4xl">
      Teste de nível<template v-if="language">: <span class="capitalize">{{ language.name_pt }}</span></template>
    </h1>

    <section v-if="finalLevel" class="mt-8 rounded-2xl bg-white p-6 shadow-sm lg:p-8" aria-live="polite">
      <p class="text-lg">
        Seu nível estimado é
      </p>

      <p class="mt-2 text-6xl font-bold text-tertiary">
        {{ finalLevel }}
      </p>

      <p class="mt-4 text-quaternary">
        Você pode confirmar esse nível ou escolher outro manualmente.
      </p>

      <div class="mt-6 flex flex-wrap gap-4">
        <ECButton color="secondary" :disabled="isSaving" @on-click="confirm">
          Confirmar
        </ECButton>

        <ECButton color="border" @on-click="chooseAnotherLevel">
          Escolher outro nível
        </ECButton>

        <ECButton color="border" @on-click="restart">
          Refazer o teste
        </ECButton>
      </div>
    </section>

    <form v-else class="mt-8" @submit.prevent="onSubmit">
      <div class="flex items-center justify-between text-quaternary">
        <span>Etapa {{ step }} de {{ LEVELS.length }}</span>
      </div>

      <div
        class="mt-2 h-2 overflow-hidden rounded-full bg-white"
        role="progressbar"
        aria-label="Progresso do teste"
        :aria-valuenow="progress"
        aria-valuemin="0"
        aria-valuemax="100"
      >
        <div class="h-full bg-secondary transition-all" :style="{ width: `${progress}%` }" />
      </div>

      <p v-if="isPending" class="mt-8">
        {{ MESSAGES.pending.placementLoad }}
      </p>

      <p v-else-if="isError" class="mt-8 text-red-700" role="alert">
        {{ MESSAGES.error.placementLoad }}
      </p>

      <template v-else-if="test">
        <fieldset
          v-for="(question, number) in test.questions"
          :key="question.id"
          class="mt-8 rounded-2xl bg-white p-6 shadow-sm"
        >
          <legend class="sr-only">
            Pergunta {{ number + 1 }}
          </legend>

          <p class="text-lg font-medium">
            {{ number + 1 }}. {{ question.prompt }}
          </p>

          <div class="mt-4 flex flex-col gap-2">
            <label
              v-for="option in question.options"
              :key="option.index"
              class="flex cursor-pointer items-center gap-3 rounded-lg border-2 border-secondary/20 px-4 py-3 transition-colors hover:border-secondary/60 has-checked:border-secondary has-checked:bg-primary/30"
            >
              <input
                v-model="answers[question.id]"
                type="radio"
                :name="question.id"
                :value="option.index"
                class="h-4 w-4 accent-secondary"
              >
              <span>{{ option.text }}</span>
            </label>
          </div>
        </fieldset>

        <div class="mt-8">
          <ECButton type="submit" color="secondary" :disabled="!canSubmit || isSubmitting">
            {{ isSubmitting ? 'Enviando...' : 'Continuar' }}
          </ECButton>
        </div>
      </template>
    </form>
  </div>
</template>
