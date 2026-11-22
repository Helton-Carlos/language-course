<script setup lang="ts">
import { ArrowLeft } from 'lucide-vue-next';
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
    <ArrowLeft class="h-5 w-5" aria-hidden="true" />
    Voltar
  </router-link>

  <button
    v-else
    type="button"
    :class="classes"
    @click="emit('onClick')"
  >
    <ArrowLeft class="h-5 w-5" aria-hidden="true" />
    Voltar
  </button>
</template>
