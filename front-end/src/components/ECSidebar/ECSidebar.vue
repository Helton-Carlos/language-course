<script setup lang="ts">
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import ECSidebarItem from '@/components/ECSidebar/ECSidebarItem.vue';
import type { ECSidebar } from '@/components/ECSidebar/Type';

const { items, title = 'Menu' } = defineProps<ECSidebar>();

const route = useRoute();
const open = ref<boolean>(false);

watch(() => route.fullPath, () => {
  open.value = false;
});
</script>

<template>
  <aside class="lg:sticky lg:top-8 lg:self-start">
    <button
      type="button"
      class="btn btn-primary w-full lg:hidden"
      :aria-expanded="open"
      aria-controls="sidebar-nav"
      @click="open = !open"
    >
      {{ title }}
    </button>

    <nav
      id="sidebar-nav"
      :aria-label="title"
      class="mt-2 rounded-2xl bg-white p-4 shadow-sm lg:mt-0 lg:block"
      :class="open ? 'block' : 'hidden'"
    >
      <h2 class="mb-3 hidden px-3 text-xs font-bold uppercase tracking-wide text-quaternary lg:block">
        {{ title }}
      </h2>

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
