<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import { languagesStore } from '@/stores/languages.ts'
import { storeToRefs } from 'pinia';
import { useRouter } from 'vue-router';

import ECButton from '@/components/ECButton/ECButton.vue';

const name = ref<string>('bem vindo');
const router = useRouter();
const store = languagesStore()
const { languages } = storeToRefs(store)

onMounted(store.fetchLanguages)

function goInit() {
  router.push({ name: 'init' })
}
</script>

<template>
  <h1 class="text-3xl font-bold underline">
    {{ name }}
  </h1>

  <p>{{ languages }}</p>

  <ECButton title="next" @onClick="goInit" />
</template>
