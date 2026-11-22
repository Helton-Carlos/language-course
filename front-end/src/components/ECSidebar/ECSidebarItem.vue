<script setup lang="ts">
import { ChevronDown } from 'lucide-vue-next';
import { ref } from 'vue';
import type { ECSidebarItem } from '@/components/ECSidebar/Type';

const { item, level = 0 } = defineProps<{
  item: ECSidebarItem;
  level?: number;
}>();

const open = ref<boolean>(true);
</script>

<template>
  <li>
    <div class="flex items-center gap-1">
      <router-link
        v-if="item.to"
        v-slot="{ href, navigate, isActive, isExactActive }"
        :to="item.to"
        custom
      >
        <a
          :href="href"
          :aria-current="(item.exact ? isExactActive : isActive) ? 'page' : undefined"
          :class="[
            'flex flex-1 items-center gap-3 rounded-lg px-3 py-2 font-medium transition-colors',
            (item.exact ? isExactActive : isActive)
              ? 'bg-primary text-tertiary'
              : 'text-quaternary hover:bg-gray',
          ]"
          @click="navigate"
        >
          <component
            :is="item.icon"
            v-if="item.icon"
            class="h-5 w-5 shrink-0"
            aria-hidden="true"
          />
          {{ item.label }}
        </a>
      </router-link>

      <button
        v-else
        type="button"
        class="flex flex-1 cursor-pointer items-center justify-between rounded-lg px-3 py-2 font-bold text-tertiary hover:bg-gray"
        :aria-expanded="open"
        @click="open = !open"
      >
        <span class="flex items-center gap-3">
          <component
            :is="item.icon"
            v-if="item.icon"
            class="h-5 w-5 shrink-0"
            aria-hidden="true"
          />
          {{ item.label }}
        </span>

        <ChevronDown class="h-4 w-4 transition-transform" :class="{ '-rotate-90': !open }" aria-hidden="true" />
      </button>

      <button
        v-if="item.to && item.children?.length"
        type="button"
        class="cursor-pointer rounded-lg p-2 text-quaternary hover:bg-gray"
        :aria-expanded="open"
        :aria-label="`${open ? 'Recolher' : 'Expandir'} ${item.label}`"
        @click="open = !open"
      >
        <ChevronDown class="h-4 w-4 transition-transform" :class="{ '-rotate-90': !open }" aria-hidden="true" />
      </button>
    </div>

    <ul
      v-if="item.children?.length && open"
      class="mt-1 flex flex-col gap-1 border-l border-tertiary/15 pl-3"
      :class="level === 0 ? 'ml-4' : 'ml-2'"
    >
      <ECSidebarItem
        v-for="child in item.children"
        :key="child.key"
        :item="child"
        :level="level + 1"
      />
    </ul>
  </li>
</template>
