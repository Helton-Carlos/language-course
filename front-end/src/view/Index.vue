<script lang="ts" setup>
import { languagesStore } from '@/stores/languages.ts'
import { storeToRefs } from 'pinia';
import { useRouter } from 'vue-router';

import ECButton from '@/components/ECButton/ECButton.vue';
import ECFooter from '@/layouts/ECFooter.vue'

const router = useRouter();
const store = languagesStore()
const { languages } = storeToRefs(store)

function goInit() {
  router.push({ name: 'init' })
}

function goLanguage(id?: string) {
  if (!id) return

  router.push({ name: 'init', params: { id } })
}
</script>

<template>
  <div class="container flex justify-between my-16">
    <div>
      <div class="w-205">
        <h3 class="text-6xl">
          Aprenda um novo idioma
          Pratique todos os dias e
          alcance seus objetivos.
        </h3>
        <p class="text-2xl my-8">
          Explore um novo idioma
          <br> Pequenos passos, grandes conquistas.
        </p>
      </div>

      <div class="flex gap-8 my-8">
        <ECButton color="border" @onClick="goInit">
          Configuração
        </ECButton>

        <ECButton color="secondary" @onClick="goLanguage">
          Login
        </ECButton>
      </div>

      <div class="bg-gray-300 w-140 flex gap-8 py-4 px-8 rounded-2xl">
        <div v-for="language in languages" :key="language.code">
          <img :src="`https://flagcdn.com/${language.prefix.toLowerCase()}.svg`" :alt="`Bandeira: ${language.name_pt}`" class="h-9 rounded-sm" />
        </div>
      </div>
    </div>

    <img src="/main-image.svg" alt="imagens de pessoas com livro" />
  </div>

  <div class="container">
    <h3 class="text-3xl font-bold">
      FAÇA SUA ESCOLHA
    </h3>

    <div class="grid grid-cols-2 grid-rows-3 my-8 lg:grid-cols-3 lg:grid-rows-1">
      <div v-for="language in languages" :key="language.code" class="group relative cursor-pointer">
        <img :src="`/${language.code}.png`" :alt="`Idioma: ${language.name_pt}`" class="w-full" />

        <div class="absolute inset-0 flex items-center justify-center bg-primary text-tertiary text-[60px] font-bold capitalize opacity-0 transition-opacity group-hover:opacity-100">
          {{ language.name_pt }}
        </div>
      </div>
    </div>
  </div>

  <div class="container my-16">
    <h3 class="text-3xl font-bold">
      SOBRE
    </h3>

    <div class="grid grid-cols-1 items-center gap-16 my-8 lg:grid-cols-2">
      <img src="/main-image.svg" alt="imagens de pessoas com livro" class="h-150" />

      <div>
        <h4 class="text-3xl font-bold">Language Course</h4>
        <p class="text-2xl font-medium">Aprenda idiomas, conquiste novas oportunidades</p>

        <p class="text-2xl my-8">O Language Course é uma plataforma desenvolvida para brasileiros que desejam aprender os principais idiomas do mundo de forma acessível, prática e intuitiva. O objetivo é tornar o aprendizado de novas línguas mais simples e ajudar cada pessoa a ampliar seus horizontes, desenvolver novas habilidades e conquistar oportunidades pessoais e profissionais.</p>

        <p class="text-2xl">A plataforma busca reunir recursos que incentivem o aprendizado contínuo, permitindo que os usuários desenvolvam seu vocabulário, aprimorem a compreensão e ganhem confiança na comunicação em outros idiomas.
          Com foco nas necessidades dos brasileiros, o Language Course pretende aproximar o ensino de idiomas da realidade de quem fala português, tornando a jornada de aprendizado mais familiar e motivadora.</p>

        <div class="flex gap-8 my-8">
          <ECButton color="border" @onClick="goInit">
            Configuração
          </ECButton>

          <ECButton color="secondary" @onClick="goLanguage">
            Login
          </ECButton>
        </div>
      </div>
    </div>
  </div>

  <ECFooter />
</template>
