<script setup lang="ts">
import type { ECFeatureCard } from '@/components/ECFeatureCard/Type';

defineProps<ECFeatureCard>();
</script>

<template>
  <router-link
    :to="to"
    class="flex h-full flex-col gap-3 rounded-2xl bg-white p-5 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"
  >
    <svg
      v-if="icon"
      viewBox="0 0 24 24"
      fill="currentColor"
      class="h-8 w-8 text-secondary"
      aria-hidden="true"
    >
      <path fill-rule="evenodd" :d="icon" />
    </svg>

    <span class="text-xl font-bold text-tertiary">
      {{ title }}
    </span>

    <span class="text-sm text-quaternary">
      {{ description }}
    </span>
  </router-link>
</template>
