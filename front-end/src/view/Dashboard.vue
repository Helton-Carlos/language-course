<script lang="ts" setup>
import { RouterView, useRoute } from 'vue-router';
import ECSidebar from '@/components/ECSidebar/ECSidebar.vue';
import ECFooter from '@/layouts/ECFooter.vue';
import { useDashboardMenu } from '@/composables/useDashboardMenu';

const route = useRoute();
const menu = useDashboardMenu();
</script>

<template>
  <div class="flex min-h-full flex-col">
    <div class="flex-1">
      <div class="container my-8 grid gap-8 lg:my-16 lg:grid-cols-[16rem_1fr]">
        <ECSidebar title="Menu" :items="menu" />

        <main class="min-w-0 self-start">
          <RouterView v-slot="{ Component }">
            <Transition name="route">
              <component :is="Component" :key="route.path" />
            </Transition>
          </RouterView>
        </main>
      </div>
    </div>

    <ECFooter />
  </div>
</template>
