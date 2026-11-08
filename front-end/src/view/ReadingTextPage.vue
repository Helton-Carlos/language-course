<script lang="ts" setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import { useReadingText } from '@/composables/useReading';
import { MESSAGES } from '@/utils/message';

const route = useRoute();

const theme = computed(() => String(route.params.tema));
const situation = computed(() => String(route.params.situacao));
const { data: text, isPending, isError } = useReadingText(theme, situation);
</script>

<template>
  <article class="max-w-3xl">
    <ECBackButton :to="{ name: 'dashboard-ler-tema', params: { tema: theme } }" />

    <p v-if="isPending" class="mt-6">
      {{ MESSAGES.pending.readingLoad }}
    </p>

    <p v-else-if="isError" class="mt-6 text-red-700" role="alert">
      {{ MESSAGES.error.readingLoad }}
    </p>

    <template v-else-if="text">
      <h1 class="mt-4 text-3xl font-bold">
        {{ text.title }}
      </h1>

      <p class="mt-6 text-xl leading-relaxed">
        {{ text.body }}
      </p>
    </template>
  </article>
</template>
