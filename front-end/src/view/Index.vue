<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import { languagesStore } from '@/stores/languages.ts'
import { storeToRefs } from 'pinia';
import { useRouter } from 'vue-router';

import ECButton from '@/components/ECButton/ECButton.vue';
import ECCard from '@/components/ECCard/ECCard.vue';

const name = ref<string>('bem vindo');
const router = useRouter();
const store = languagesStore()
const { languages } = storeToRefs(store)

function goInit() {
  router.push({ name: 'init' })
}

onMounted(store.fetchLanguages)
</script>

<template>
  <h1 class="text-3xl font-bold underline">
    {{ name }}
  </h1>

  <div v-for="language in languages" :key="language.code">
    <ECCard>
      <template #body>
        <div class="flex items-center gap-3">
          <img :src="`https://flagcdn.com/${language.prefix.toLowerCase()}.svg`" :alt="`Bandeira: ${language.name_pt}`" class="h-5 w-8 rounded-sm object-cover" />

          <span>{{ language.name }}</span> |
          <span class="text-quaternary capitalize">{{ language.name_pt }}</span>
        </div>
      </template>
    </ECCard>
  </div>

  <ECButton title="next" @onClick="goInit" />
</template>
