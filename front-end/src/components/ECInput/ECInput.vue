<script setup lang="ts">
import type { ECInput } from '@/components/ECInput/Type';

const {
  id,
  label,
  placeholder,
  type = 'text',
  disabled = false,
  required = false,
  autocomplete,
  error,
} = defineProps<ECInput>();

const model = defineModel<string>();
</script>

<template>
  <div class="flex flex-col gap-1">
    <label v-if="label" :for="id" class="font-medium text-tertiary">
      {{ label }}
    </label>

    <input
      :id="id"
      v-model="model"
      :type="type"
      :placeholder="placeholder"
      :disabled="disabled"
      :required="required"
      :autocomplete="autocomplete"
      :aria-invalid="error ? true : undefined"
      :aria-describedby="error ? `${id}-error` : undefined"
      class="w-full rounded-md border-2 bg-white px-4 py-2 text-tertiary placeholder:text-quaternary/60 outline-none transition-colors focus:ring-4 focus:ring-primary disabled:cursor-not-allowed disabled:opacity-50"
      :class="error ? 'border-red-700' : 'border-secondary/30 focus:border-secondary'"
    />

    <p
      v-if="error"
      :id="`${id}-error`"
      class="text-red-700"
      role="alert"
    >
      {{ error }}
    </p>
  </div>
</template>
