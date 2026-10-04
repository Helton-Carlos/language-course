<script lang="ts" setup>
import { ref } from 'vue';
import ECButton from '../components/ECButton/ECButton.vue';

const name = ref<string>('init');
</script>

<template>
  <h1 class="text-3xl font-bold underline">
    {{ name }}
  </h1>
  <ECButton :title="name" />
</template>
