<script setup lang="ts">
import { X } from 'lucide-vue-next';
import { useToast, type ToastAction, type ToastType } from '@/composables/useToast';

const { toasts, dismiss } = useToast();

function runAction(id: number, action: ToastAction) {
  dismiss(id);
  action.onClick?.();
}

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
        <div class="flex-1">
          <p class="font-medium">
            {{ item.message }}
          </p>
          <div v-if="item.actions?.length" class="mt-3 flex gap-2">
            <button
              v-for="action in item.actions"
              :key="action.label"
              type="button"
              :class="[
                'cursor-pointer rounded px-3 py-1 font-medium transition-colors',
                action.primary ? 'bg-secondary text-white hover:bg-secondary-hover' : 'bg-black/10 hover:bg-black/20',
              ]"
              @click="runAction(item.id, action)"
            >
              {{ action.label }}
            </button>
          </div>
        </div>

        <button
          type="button"
          class="cursor-pointer rounded p-1 hover:bg-black/15"
          aria-label="Fechar notificação"
          @click="dismiss(item.id)"
        >
          <X class="h-4 w-4" aria-hidden="true" />
        </button>
      </div>
    </TransitionGroup>
  </div>
</template>
