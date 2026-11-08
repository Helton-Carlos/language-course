<script lang="ts" setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import ECFeatureCard from '@/components/ECFeatureCard/ECFeatureCard.vue';
import { useReadingSituations, useReadingThemes } from '@/composables/useReading';
import { MESSAGES } from '@/utils/message';

const route = useRoute();

const theme = computed(() => String(route.params.tema));
const { data: themes } = useReadingThemes();
const { data: situations, isPending, isError } = useReadingSituations(theme);

const themeLabel = computed(() => themes.value?.find((item) => item.key === theme.value)?.label ?? '');
</script>

<template>
  <section>
    <ECBackButton :to="{ name: 'dashboard-ler' }" />

    <h1 class="mt-4 text-3xl font-bold">
      {{ themeLabel }}
    </h1>

    <p class="mt-2 text-quaternary">
      Escolha uma situação para ler.
    </p>

    <p v-if="isPending" class="mt-6">
      {{ MESSAGES.pending.readingLoad }}
    </p>

    <p v-else-if="isError" class="mt-6 text-red-700" role="alert">
      {{ MESSAGES.error.readingLoad }}
    </p>

    <ul v-else class="mt-6 grid gap-4 sm:grid-cols-2">
      <li v-for="situation in situations" :key="situation.key">
        <ECFeatureCard
          :to="{ name: 'dashboard-ler-texto', params: { tema: theme, situacao: situation.key } }"
          :title="situation.title"
          :description="situation.description"
        />
      </li>
    </ul>
  </section>
</template>
