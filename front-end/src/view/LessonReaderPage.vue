<script lang="ts" setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import ECLesson from '@/components/ECLesson/ECLesson.vue';
import { useLesson } from '@/composables/useLessons';
import { MESSAGES } from '@/utils/message';

const route = useRoute();
const id = computed(() => String(route.params.id));

const { data: lesson, isPending, isError } = useLesson(id);
</script>

<template>
  <article>
    <ECBackButton :to="{ name: 'dashboard-biblioteca' }" />
    <p v-if="isPending" class="mt-6">
      {{ MESSAGES.pending.lessonLoad }}
    </p>
    <p v-else-if="isError" class="mt-6 text-red-700" role="alert">
      {{ MESSAGES.error.lessonLoad }}
    </p>
    <ECLesson v-else-if="lesson" :title="lesson.title" :body="lesson.body" />
  </article>
</template>
