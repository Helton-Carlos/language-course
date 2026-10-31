<script lang="ts" setup>
import { computed, ref } from 'vue'
import ECButton from '@/components/ECButton/ECButton.vue';
import { useRoute, useRouter } from 'vue-router';
import { languagesStore } from '@/stores/languages.ts'
import { storeToRefs } from 'pinia';
import { LEVELS } from '@/utils/levels'

const route = useRoute()
const router = useRouter()
const store = languagesStore()
const { languages } = storeToRefs(store)

const selectedLevel = ref<(typeof LEVELS)[number]>('B2')

const language = computed(() => {
  const id = String(route.params.id)

  return languages.value.find((item) => item.id === id)
})

function goBack() {
  router.push({ name: 'idiomas' })
}
</script>

<template>
  <div class="container mt-16 grid gap-10 lg:grid-cols-2">
    <div>
      <h2 class="text-4xl lg:text-5xl">
        Otima escolha o
        <span class="relative inline-block">
          <span class="uppercase font-bold">{{ language?.name_pt }}</span>,
          <img
            src="/icon-risk.svg"
            alt="risco ilustrativo"
            class="pointer-events-none absolute bottom-full left-full w-[1.1em] translate-y-[0.15em]"
          >
        </span>
        <br>é utilizado em diversos paises
        <br>na américa do sul.
      </h2>

      <p class="my-4 text-2xl">
        Agora queremos saber seu nível
      </p>

      <div role="group" aria-labelledby="level-label">
        <span id="level-label" class="text-2xl">Level:</span>

        <div class="my-4 flex flex-wrap gap-4">
          <button
            v-for="level in LEVELS"
            :key="level"
            type="button"
            :aria-pressed="selectedLevel === level"
            :class="[
              'cursor-pointer rounded px-3 py-2 text-2xl transition-colors',
              selectedLevel === level
                ? 'bg-secondary text-white'
                : 'bg-white/60 text-tertiary hover:bg-white',
            ]"
            @click="selectedLevel = level"
          >
            {{ level }}
          </button>
        </div>

        <ECButton color="border" @on-click="goBack">
          Avançar
        </ECButton>
      </div>

      <p class="mt-8 text-2xl">
        Não sei meu nível?
      </p>

      <div class="mt-2 flex gap-4">
        <ECButton color="border" @on-click="goBack">
          Voltar
        </ECButton>

        <ECButton color="secondary">
          Teste
        </ECButton>
      </div>
    </div>

    <figure class="w-full max-w-sm justify-self-end rounded-lg bg-[#d9d9d9] p-5">
      <img
        :src="`https://flagcdn.com/${language?.prefix?.toLowerCase()}.svg`"
        :alt="`Bandeira: ${language?.name_pt}`"
        class="aspect-3/2 w-full object-cover"
      />

      <figcaption class="mt-3 text-xs">
        {{ language?.name_pt }}, {{ language?.prefix }}
      </figcaption>
    </figure>
  </div>
</template>
