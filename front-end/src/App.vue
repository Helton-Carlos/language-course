<script setup lang="ts">
import { RouterView } from 'vue-router';
import ECHeader from '@/layouts/ECHeader.vue';

</script>

<template>
  <div class="grid min-h-screen grid-rows-[auto_1fr]">
    <ECHeader />

    <div>
      <RouterView />
    </div>
  </div>
</template>
