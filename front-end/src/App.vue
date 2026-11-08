<script setup lang="ts">
import { RouterView, useRoute } from 'vue-router';
import ECHeader from '@/layouts/ECHeader.vue';
import ECToaster from '@/components/ECToast/ECToaster.vue';

const route = useRoute();
</script>

<template>
  <div class="grid min-h-screen grid-rows-[auto_1fr]">
    <ECHeader />

    <div>
      <RouterView v-slot="{ Component }">
        <Transition name="route">
          <component :is="Component" :key="route.matched[0]?.path ?? route.path" />
        </Transition>
      </RouterView>
    </div>
  </div>

  <ECToaster />
</template>
