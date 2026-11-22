<script setup lang="ts">
import { X } from 'lucide-vue-next';
import { onBeforeUnmount, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import ECSidebarItem from '@/components/ECSidebar/ECSidebarItem.vue';
import type { ECSidebar } from '@/components/ECSidebar/Type';
import { useMobileMenu } from '@/composables/useMobileMenu';

const { items, title = 'Menu' } = defineProps<ECSidebar>();

const route = useRoute();
const { isOpen, close } = useMobileMenu();

function closeOnEscape(event: KeyboardEvent): void {
  if (event.key === 'Escape') close();
}

onMounted(() => {
  window.addEventListener('keydown', closeOnEscape);
});

onBeforeUnmount(() => {
  window.removeEventListener('keydown', closeOnEscape);
  close();
});

watch(() => route.fullPath, close);
</script>

<template>
  <aside class="contents lg:sticky lg:top-8 lg:block lg:self-start">
    <div
      v-if="isOpen"
      class="fixed inset-0 z-30 bg-black/40 lg:hidden"
      aria-hidden="true"
      @click="close"
    />
    <nav
      id="sidebar-nav"
      :aria-label="title"
      :class="[
        'fixed inset-y-0 left-0 z-40 w-72 max-w-[85vw] overflow-y-auto bg-white p-4 shadow-lg transition-transform duration-200 motion-reduce:transition-none',
        'lg:static lg:z-auto lg:w-auto lg:max-w-none lg:translate-x-0 lg:overflow-visible lg:rounded-2xl lg:shadow-sm',
        isOpen ? 'translate-x-0' : 'invisible -translate-x-full lg:visible',
      ]"
    >
      <div class="mb-3 flex items-center justify-between px-3">
        <h2 class="text-xs font-bold uppercase tracking-wide text-quaternary">
          {{ title }}
        </h2>
        <button
          type="button"
          class="cursor-pointer rounded-md p-1 text-quaternary transition-colors hover:bg-primary-light lg:hidden"
          aria-label="Fechar menu"
          @click="close"
        >
          <X class="h-5 w-5" aria-hidden="true" />
        </button>
      </div>
      <ul class="flex flex-col gap-1">
        <ECSidebarItem
          v-for="item in items"
          :key="item.key"
          :item="item"
        />
      </ul>
    </nav>
  </aside>
</template>