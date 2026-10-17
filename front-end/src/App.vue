<script setup lang="ts">
import { RouterView } from 'vue-router';
import { computed } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

const title = computed(() => {
  return route.meta?.title
})
</script>

<template>
  <h1 class="text-3xl text-center font-bold m-8">
    {{ title }}
  </h1>

  <div class="max-w-780">
    <RouterView />
  </div>
</template>
