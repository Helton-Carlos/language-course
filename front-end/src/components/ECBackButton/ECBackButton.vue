<script setup lang="ts">
import { computed } from 'vue';
import type { ECBackButton } from '@/components/ECBackButton/Type';

const { variant = 'link' } = defineProps<ECBackButton>();

const emit = defineEmits<{
  (e: 'onClick'): void;
}>();

const classes = computed(() => [
  'inline-flex cursor-pointer items-center gap-2',
  variant === 'button'
    ? 'btn btn-border justify-center'
    : 'font-medium text-quaternary transition-colors hover:text-tertiary',
]);
</script>

<template>
  <router-link v-if="to" :to="to" :class="classes">
    <svg
      viewBox="0 0 24 24"
      fill="currentColor"
      class="h-5 w-5"
      aria-hidden="true"
    >
      <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2Z" />
    </svg>
    Voltar
  </router-link>

  <button
    v-else
    type="button"
    :class="classes"
    @click="emit('onClick')"
  >
    <svg
      viewBox="0 0 24 24"
      fill="currentColor"
      class="h-5 w-5"
      aria-hidden="true"
    >
      <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2Z" />
    </svg>
    Voltar
  </button>
</template>
