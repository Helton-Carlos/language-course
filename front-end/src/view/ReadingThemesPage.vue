<script lang="ts" setup>
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import ECFeatureCard from '@/components/ECFeatureCard/ECFeatureCard.vue';
import { useReadingThemes } from '@/composables/useReading';
import { MESSAGES } from '@/utils/message';

const { data: themes, isPending, isError } = useReadingThemes();
</script>

<template>
  <section>
    <ECBackButton :to="{ name: 'dashboard' }" />

    <h1 class="mt-4 text-3xl font-bold">
      Ler
    </h1>

    <p class="mt-2 text-quaternary">
      Escolha um tema para começar.
    </p>

    <p v-if="isPending" class="mt-6">
      {{ MESSAGES.pending.readingLoad }}
    </p>

    <p v-else-if="isError" class="mt-6 text-red-700" role="alert">
      {{ MESSAGES.error.readingLoad }}
    </p>

    <ul v-else class="mt-6 grid gap-4 sm:grid-cols-2">
      <li v-for="theme in themes" :key="theme.key">
        <ECFeatureCard
          :to="{ name: 'dashboard-ler-tema', params: { tema: theme.key } }"
          :title="theme.label"
          :description="theme.description"
        />
      </li>
    </ul>
  </section>
</template>
