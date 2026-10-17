<script setup lang="ts">
import { computed } from 'vue';
import type { ECButton, ECButtonColor } from '@/components/ECButton/Type';

const {
  title = 'Título padrão',
  color = 'primary',
  type = 'button',
  disabled = false,
} = defineProps<ECButton>();

const emit = defineEmits<{
  (e: 'onClick'): void;
}>();

const colorClasses: Record<ECButtonColor, string> = {
  primary: 'btn-primary',
  secondary: 'btn-secondary',
};

const buttonClasses = computed(() => [
  'btn',
  colorClasses[color],
  { 'btn-disabled': disabled },
]);
</script>

<template>
  <button
    :type="type"
    :class="buttonClasses"
    :disabled="disabled"
    @click="emit('onClick')"
  >
    {{ title }}
  </button>
</template>
