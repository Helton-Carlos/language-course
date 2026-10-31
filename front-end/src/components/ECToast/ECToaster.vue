<script setup lang="ts">
import { useToast, type ToastType } from '@/composables/useToast';

const { toasts, dismiss } = useToast();

const typeClasses: Record<ToastType, string> = {
  error: 'bg-red-700 text-white',
  success: 'bg-green-700 text-white',
  warning: 'bg-primary text-tertiary',
  info: 'bg-blue-700 text-white',
};
</script>

<template>
  <div class="pointer-events-none fixed inset-x-4 bottom-4 z-50 flex flex-col items-start gap-2 sm:right-auto sm:w-96">
    <TransitionGroup
      enter-active-class="transition duration-200 motion-reduce:transition-none"
      enter-from-class="-translate-x-4 opacity-0"
      leave-active-class="transition duration-150 motion-reduce:transition-none"
      leave-to-class="opacity-0"
      move-class="transition duration-200 motion-reduce:transition-none"
    >
      <div
        v-for="item in toasts"
        :key="item.id"
        :role="item.type === 'error' ? 'alert' : 'status'"
        class="pointer-events-auto flex w-full items-start gap-3 rounded-lg p-4 shadow-lg"
        :class="typeClasses[item.type]"
      >
        <p class="flex-1 font-medium">
          {{ item.message }}
        </p>

        <button
          type="button"
          class="cursor-pointer rounded p-1 hover:bg-black/15"
          aria-label="Fechar notificação"
          @click="dismiss(item.id)"
        >
          <svg
            viewBox="0 0 20 20"
            fill="currentColor"
            class="h-4 w-4"
            aria-hidden="true"
          >
            <path d="M5.3 5.3a1 1 0 0 1 1.4 0L10 8.6l3.3-3.3a1 1 0 1 1 1.4 1.4L11.4 10l3.3 3.3a1 1 0 0 1-1.4 1.4L10 11.4l-3.3 3.3a1 1 0 0 1-1.4-1.4L8.6 10 5.3 6.7a1 1 0 0 1 0-1.4Z" />
          </svg>
        </button>
      </div>
    </TransitionGroup>
  </div>
</template>
