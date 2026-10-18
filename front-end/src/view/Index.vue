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
  <div class="container flex flex-col gap-8 my-8 lg:flex-row lg:justify-between lg:my-16">
    <div>
      <div class="lg:w-205">
        <h3 class="text-4xl lg:text-6xl">
          Aprenda um novo idioma
          Pratique todos os dias e
          alcance seus objetivos.
        </h3>
        <p class="text-xl my-6 lg:text-2xl lg:my-8">
          Explore um novo idioma
          <br> Pequenos passos, grandes conquistas.
        </p>
      </div>

      <div class="flex flex-wrap gap-4 my-6 lg:gap-8 lg:my-8">
        <ECButton color="border" @onClick="goInit">
          Documentação
        </ECButton>

        <ECButton color="secondary" @onClick="goLanguage">
          Login
        </ECButton>
      </div>

      <div class="bg-gray-300 w-full flex flex-wrap justify-center gap-4 py-4 px-4 rounded-2xl lg:w-150 lg:justify-start lg:gap-8 lg:px-8">
        <div v-for="language in languages" :key="language.code">
          <img :src="`https://flagcdn.com/${language.prefix.toLowerCase()}.svg`" :alt="`Bandeira: ${language.name_pt}`" class="h-9 rounded-sm" />
        </div>
      </div>
    </div>

    <img src="/main-image.svg" alt="imagens de pessoas com livro" class="w-full max-w-md mx-auto lg:w-auto lg:max-w-none lg:mx-0" />
  </div>

  <div class="container">
    <h3 class="text-3xl font-bold">
      FAÇA SUA ESCOLHA
    </h3>

    <div class="grid grid-cols-2 grid-rows-3 my-8 lg:grid-cols-3 lg:grid-rows-1">
      <div v-for="language in languages" :key="language.code" class="group relative cursor-pointer">
        <img :src="`/${language.code}.png`" :alt="`Idioma: ${language.name_pt}`" class="w-full" />

        <div class="absolute inset-0 flex items-center justify-center bg-primary text-tertiary text-2xl font-bold capitalize opacity-0 transition-opacity group-hover:opacity-100 lg:text-[60px]">
          {{ language.name_pt }}
        </div>
      </div>
    </div>
  </div>

  <div class="container my-8 lg:my-16">
    <h3 class="text-3xl font-bold">
      SOBRE
    </h3>

    <div class="grid grid-cols-1 items-center gap-8 my-8 lg:grid-cols-2 lg:gap-16">
      <img src="/main-image.svg" alt="imagens de pessoas com livro" class="h-72 mx-auto lg:h-150" />

      <div>
        <h4 class="text-3xl font-bold">Language Course</h4>
        <p class="text-xl font-medium lg:text-2xl">Aprenda idiomas, conquiste novas oportunidades</p>

        <p class="text-lg my-6 lg:text-2xl lg:my-8">O Language Course é uma plataforma desenvolvida para brasileiros que desejam aprender os principais idiomas do mundo de forma acessível, prática e intuitiva. O objetivo é tornar o aprendizado de novas línguas mais simples e ajudar cada pessoa a ampliar seus horizontes, desenvolver novas habilidades e conquistar oportunidades pessoais e profissionais.</p>

        <p class="text-lg lg:text-2xl">A plataforma busca reunir recursos que incentivem o aprendizado contínuo, permitindo que os usuários desenvolvam seu vocabulário, aprimorem a compreensão e ganhem confiança na comunicação em outros idiomas.
          Com foco nas necessidades dos brasileiros, o Language Course pretende aproximar o ensino de idiomas da realidade de quem fala português, tornando a jornada de aprendizado mais familiar e motivadora.</p>

        <div class="flex flex-wrap gap-4 my-6 lg:gap-8 lg:my-8">
          <ECButton color="border" @onClick="goInit">
            Documentação
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
