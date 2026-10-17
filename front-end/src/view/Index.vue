<script lang="ts" setup>
import { ref } from 'vue';
import ECButton from '../components/ECButton/ECButton.vue';
import { useRouter } from 'vue-router';

const name = ref<string>('bem vindo');
const router = useRouter();

function goInit() {
  router.push({ name: 'init' })
}
</script>

<template>
  <h1 class="text-3xl font-bold underline">
    {{ name }}
  </h1>

  <ECButton :title="name" @onClick="goInit" />
</template>
