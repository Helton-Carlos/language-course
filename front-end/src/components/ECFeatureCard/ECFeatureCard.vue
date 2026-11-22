<script setup lang="ts">
import type { ECFeatureCard } from '@/components/ECFeatureCard/Type';

defineProps<ECFeatureCard>();
</script>

<template>
  <router-link
    :to="to"
    class="flex h-full flex-col gap-3 rounded-2xl bg-white p-5 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"
  >
    <component
      :is="icon"
      v-if="icon"
      class="h-8 w-8 text-primary"
      aria-hidden="true"
    />

    <span class="text-xl font-bold text-tertiary">
      {{ title }}
    </span>

    <span class="text-quaternary">
      {{ description }}
    </span>
  </router-link>
</template>
