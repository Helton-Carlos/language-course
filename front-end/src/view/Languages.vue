<script lang="ts" setup>
import { useRouter } from 'vue-router';
import { languagesStore } from '@/stores/languages.ts'
import { storeToRefs } from 'pinia';

const router = useRouter()
const store = languagesStore()
const { languages } = storeToRefs(store)

function getLanguage(id?: string) {
  if (!id) return
  router.push({ name: 'init', params: { id } })
}
</script>

<template>
  <div class="container">
    <h3 class="text-3xl font-bold mt-16">
      FAÇA SUA ESCOLHA
    </h3>

    <div class="grid grid-cols-2 grid-rows-3 my-8 lg:grid-cols-3 lg:grid-rows-1">
      <div
        v-for="language in languages"
        :key="language.code"
        class="group relative cursor-pointer"
        @click="getLanguage(language.id)"
      >
        <img :src="`/${language.code}.png`" :alt="`Idioma: ${language.name_pt}`" class="w-full" />

        <div class="absolute inset-0 flex items-center justify-center bg-primary text-tertiary text-2xl font-bold capitalize opacity-0 transition-opacity group-hover:opacity-100 lg:text-[60px]">
          {{ language.name_pt }}
        </div>
      </div>
    </div>
  </div>
</template>
