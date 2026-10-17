<script lang="ts" setup>
import { computed } from 'vue'
import ECButton from '@/components/ECButton/ECButton.vue';
import { useRoute } from 'vue-router';
import { languagesStore } from '@/stores/languages.ts'
import { storeToRefs } from 'pinia';

const route = useRoute()
const store = languagesStore()
const { languages } = storeToRefs(store)

const language = computed(() => {
  const id = String(route.params.id)

  return languages.value.find((item) => item.id === id)
})
</script>

<template>
  <div class="flex flex-col items-center gap-8">
    <h1 class="text-3xl font-bold text-center">
      Você escolheu o {{ language?.name }}
    </h1>

    <img :src="`https://flagcdn.com/${language?.prefix?.toLowerCase()}.svg`" :alt="`Bandeira: ${language?.name_pt}`" class="h-25 w-32 rounded-sm object-cover" />

    <ECButton title="next" />
  </div>
</template>
