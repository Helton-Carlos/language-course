<script setup lang="ts">
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import type { ECPageHeader } from '@/components/ECPageHeader/Type';

defineProps<ECPageHeader>();

defineSlots<{
  title?(): unknown;
  description?(): unknown;
  actions?(): unknown;
}>();
</script>

<template>
  <header>
    <ECBackButton v-if="backTo" :to="backTo" />
    <div
      class="flex flex-wrap items-center justify-between gap-4"
      :class="{ 'mt-4': backTo }"
    >
      <div class="min-w-0">
        <div class="flex items-center gap-4">
          <component
            :is="icon"
            v-if="icon"
            class="h-10 w-10 shrink-0 text-primary"
            aria-hidden="true"
          />
          <h1 v-if="title || $slots.title" class="text-3xl font-bold">
            <slot name="title">
              {{ title }}
            </slot>
          </h1>
        </div>
        <p v-if="description || $slots.description" class="mt-2 text-quaternary">
          <slot name="description">
            {{ description }}
          </slot>
        </p>
      </div>
      <slot name="actions" />
    </div>
  </header>
</template>