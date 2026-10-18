<script setup lang="ts">
import { RouterView } from 'vue-router';
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import ECHeader from '@/layouts/ECHeader.vue';

const route = useRoute();

const title = computed(() => {
  return route.meta?.title
})
</script>

<template>
  <ECHeader />

  <h1 class="text-3xl text-center font-bold m-8">
    {{ title }}
  </h1>

  <div class="max-w-780">
    <RouterView />
  </div>
</template>
