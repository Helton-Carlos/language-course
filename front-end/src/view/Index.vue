<script lang="ts" setup>
import { onMounted } from 'vue';
import { languagesStore } from '@/stores/languages.ts'
import { storeToRefs } from 'pinia';
import { useRouter } from 'vue-router';

import ECButton from '@/components/ECButton/ECButton.vue';
import ECCard from '@/components/ECCard/ECCard.vue';

const router = useRouter();
const store = languagesStore()
const { languages } = storeToRefs(store)

function goInit() {
  router.push({ name: 'init' })
}

onMounted(store.fetchLanguages)
</script>

<template>
  <div class="flex flex-wrap justify-center gap-4">
    <div v-for="language in languages" :key="language.code">
      <ECCard>
        <template #body>
          <div class="flex flex-col items-center gap-3">
            <img :src="`https://flagcdn.com/${language.prefix.toLowerCase()}.svg`" :alt="`Bandeira: ${language.name_pt}`" class="h-5 w-8 rounded-sm object-cover" />

            <div>
              <span>{{ language.name }}</span> |
              <span class="text-quaternary capitalize">{{ language.name_pt }}</span>
            </div>
          </div>
        </template>
      </ECCard>
    </div>
  </div>

  <div class="flex justify-center gap-8 my-8">
    <ECButton title="next" @onClick="goInit" />

    <ECButton title="next" @onClick="goInit" />
  </div>
</template>
