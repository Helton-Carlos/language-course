<script lang="ts" setup>
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import ECFeatureCard from '@/components/ECFeatureCard/ECFeatureCard.vue';
import { useDeleteLesson, useLessons } from '@/composables/useLessons';
import { useReadingThemes } from '@/composables/useReading';
import { toast } from '@/composables/useToast';
import { CONTENTS } from '@/utils/contents';
import { formatDate } from '@/utils/dates';
import { MESSAGES } from '@/utils/message';

const { data: lessons, isPending, isError } = useLessons();
const { data: themes } = useReadingThemes();
const { mutate: removeLesson, isPending: isRemoving } = useDeleteLesson();

function confirmRemove(id: string, title: string) {
  toast.confirm(`Remover o texto "${title}"?`, () => removeLesson(id), 'Remover');
}
</script>

<template>
  <section>
    <ECBackButton :to="{ name: 'dashboard' }" />
    <div class="mt-4 flex flex-wrap items-center justify-between gap-4">
      <div>
        <h1 class="text-3xl font-bold">
          Biblioteca
        </h1>
        <p class="mt-2 text-quaternary">
          Seus textos, leituras por tema e outros conteúdos em inglês.
        </p>
      </div>
      <router-link :to="{ name: 'dashboard-biblioteca-importar' }" class="btn btn-secondary">
        Importar texto
      </router-link>
    </div>

    <h2 class="mt-10 text-xl font-bold">
      Meus textos
    </h2>
    <p v-if="isPending" class="mt-4">
      {{ MESSAGES.pending.lessonsLoad }}
    </p>
    <p v-else-if="isError" class="mt-4 text-red-700" role="alert">
      {{ MESSAGES.error.lessonsLoad }}
    </p>
    <div v-else-if="!lessons?.length" class="mt-4 rounded-2xl bg-white p-6 shadow-sm">
      <p class="font-medium text-tertiary">
        Você ainda não importou nenhum texto.
      </p>
      <p class="mt-1 text-quaternary">
        Cole uma notícia, letra de música ou artigo em inglês para estudar com o seu vocabulário.
      </p>
    </div>
    <ul v-else class="mt-4 grid gap-4 md:grid-cols-2">
      <li
        v-for="lesson in lessons"
        :key="lesson.id"
        class="flex flex-col gap-2 rounded-2xl bg-white p-5 shadow-sm"
      >
        <router-link
          :to="{ name: 'dashboard-biblioteca-texto', params: { id: lesson.id } }"
          class="text-xl font-bold text-tertiary hover:underline"
        >
          {{ lesson.title }}
        </router-link>
        <p class="text-quaternary">
          {{ lesson.preview }}
        </p>
        <div class="mt-auto flex items-center justify-between pt-2 text-quaternary">
          <span>{{ lesson.word_count }} palavras · {{ formatDate(lesson.created_at) }}</span>
          <button
            type="button"
            class="cursor-pointer font-medium text-red-700 hover:underline disabled:cursor-not-allowed disabled:opacity-50"
            :disabled="isRemoving"
            @click="confirmRemove(lesson.id, lesson.title)"
          >
            Remover
          </button>
        </div>
      </li>
    </ul>

    <h2 class="mt-10 text-xl font-bold">
      Leituras por tema
    </h2>
    <ul class="mt-4 grid gap-4 sm:grid-cols-2">
      <li v-for="theme in themes" :key="theme.key">
        <ECFeatureCard
          :to="{ name: 'dashboard-ler-tema', params: { tema: theme.key } }"
          :title="theme.label"
          :description="theme.description"
        />
      </li>
    </ul>

    <h2 class="mt-10 text-xl font-bold">
      Mais conteúdos
    </h2>
    <ul class="mt-4 grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
      <li v-for="content in CONTENTS" :key="content.key">
        <ECFeatureCard
          :to="{ name: content.routeName }"
          :title="content.label"
          :description="content.description"
          :icon="content.icon"
        />
      </li>
    </ul>
  </section>
</template>
