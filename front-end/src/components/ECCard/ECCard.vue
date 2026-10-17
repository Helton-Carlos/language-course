<script setup lang="ts">
import { computed } from 'vue';
import type { ECCard } from '@/components/ECCard/Type';

const { width = '250px', clickable = false } = defineProps<ECCard>();

defineSlots<{
  header?(): unknown;
  body?(): unknown;
  footer?(): unknown;
}>();

const emit = defineEmits<{
  (e: 'onClick'): void;
}>();

const cardWidth = computed(() =>
  typeof width === 'number' ? `${width}px` : width,
);

const cardClasses = computed(() => [
  'bg-white rounded-lg border border-tertiary/15 shadow-sm',
  {
    'cursor-pointer transition duration-200 hover:-translate-y-0.5 hover:shadow-md hover:border-tertiary/30 focus-visible:outline-2 focus-visible:outline-offset-2':
      clickable,
  },
]);
</script>

<template>
  <div
    :style="{ width: cardWidth }"
    :class="cardClasses"
    :role="clickable ? 'button' : undefined"
    :tabindex="clickable ? 0 : undefined"
    @click="emit('onClick')"
    @keydown.enter.self="clickable && emit('onClick')"
    @keydown.space.self.prevent="clickable && emit('onClick')"
  >
    <header v-if="$slots.header" class="border-b border-tertiary/15 px-4 py-3 font-semibold text-tertiary">
      <slot name="header" />
    </header>

    <div v-if="$slots.body" class="flex-1 px-4 py-4 text-quaternary">
      <slot name="body" />
    </div>

    <footer v-if="$slots.footer" class="border-t border-tertiary/15 px-4 py-3">
      <slot name="footer" />
    </footer>
  </div>
</template>
