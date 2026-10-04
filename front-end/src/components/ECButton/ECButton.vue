<script setup lang="ts">
import { computed } from 'vue';
import type { ECButton, ECButtonColor } from './Type';

const props = withDefaults(defineProps<ECButton>(), {
  title: 'Título padrão',
  color: 'primary',
  type: 'button',
  disabled: false,
});

const emit = defineEmits<{
  (e: 'onClick'): void;
}>();

const colorClasses: Record<ECButtonColor, string> = {
  primary: 'btn-primary',
  secondary: 'btn-secondary',
};

const buttonClasses = computed(() => [
  'btn',
  colorClasses[props.color ?? 'primary'],
  { 'btn-disabled': props.disabled },
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
