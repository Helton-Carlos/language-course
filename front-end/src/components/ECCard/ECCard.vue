<script setup lang="ts">
import { computed } from 'vue';
import type { ECCard } from '@/components/ECCard/Type';

const { width = '250px' } = defineProps<ECCard>();

defineSlots<{
  header?(): unknown;
  body?(): unknown;
  footer?(): unknown;
}>();

const cardWidth = computed(() =>
  typeof width === 'number' ? `${width}px` : width,
);
</script>

<template>
  <article :style="{ width: cardWidth }" class="bg-white rounded-lg border border-tertiary/15 shadow-sm">
    <header v-if="$slots.header" class="border-b border-tertiary/15 px-4 py-3 font-semibold text-tertiary">
      <slot name="header" />
    </header>

    <div v-if="$slots.body" class="flex-1 px-4 py-4 text-quaternary">
      <slot name="body" />
    </div>

    <footer v-if="$slots.footer" class="border-t border-tertiary/15 px-4 py-3">
      <slot name="footer" />
    </footer>
  </article>
</template>
