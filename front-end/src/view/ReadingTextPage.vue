<script lang="ts" setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import ECLesson from '@/components/ECLesson/ECLesson.vue';
import { useReadingText } from '@/composables/useReading';
import { MESSAGES } from '@/utils/message';

const route = useRoute();
const theme = computed(() => String(route.params.tema));
const situation = computed(() => String(route.params.situacao));

const { data: text, isPending, isError } = useReadingText(theme, situation);
</script>

<template>
  <article>
    <ECBackButton :to="{ name: 'dashboard-ler-tema', params: { tema: theme } }" />
    <p v-if="isPending" class="mt-6">
      {{ MESSAGES.pending.readingLoad }}
    </p>
    <p v-else-if="isError" class="mt-6 text-red-700" role="alert">
      {{ MESSAGES.error.readingLoad }}
    </p>
    <ECLesson v-else-if="text" :title="text.title" :body="text.body" />
  </article>
</template>
