<script lang="ts" setup>
import { ENGLISH_FIRST_LANGUAGE_COUNTRIES } from '@/utils/englishFirstLanguage'

import ECFooter from '@/layouts/ECFooter.vue'
</script>

<template>
  <main class="container flex flex-col gap-8 my-8 lg:flex-row lg:justify-between lg:my-16">
    <div>
      <div class="lg:w-205">
        <h3 class="text-4xl lg:text-6xl">
          Aprenda inglês
          <br>Pratique todos os dias e
          <br> alcance seus objetivos.
        </h3>
        <p class="text-xl my-6 lg:text-2xl lg:my-8">
          Explore um novo idioma
          <br> Pequenos passos, grandes conquistas.
        </p>
      </div>

      <div class="flex flex-wrap gap-4 my-6 lg:gap-8 lg:my-8">
        <router-link class="btn btn-border" to="/documentacao">
          Documentação
        </router-link>

        <router-link class="btn btn-secondary" to="/login">
          Login
        </router-link>
      </div>

      <div class="bg-gray-300 w-full flex flex-wrap justify-center gap-4 py-4 px-4 rounded-2xl lg:w-135 lg:justify-start lg:gap-6 lg:px-8">
        <img
          v-for="country in ENGLISH_FIRST_LANGUAGE_COUNTRIES"
          :key="country.code"
          :src="`https://flagcdn.com/${country.code.toLowerCase()}.svg`"
          :alt="`Bandeira: ${country.name}`"
          :title="country.name"
          class="h-9 w-14 rounded-sm object-cover"
        />
      </div>
    </div>

    <img src="/main-image.svg" alt="imagens de pessoas com livro" class="w-full max-w-md mx-auto lg:w-auto lg:max-w-none lg:mx-0" />
  </main>

  <section class="container">
    <h3 class="text-3xl font-bold">
      LISTA DE PAÍSES QUE USAM INGLÊS
    </h3>

    <div class="grid grid-cols-2 my-8 lg:grid-cols-3">
      <div
        v-for="country in ENGLISH_FIRST_LANGUAGE_COUNTRIES"
        :key="country.code"
        class="group relative overflow-hidden"
      >
        <img
          :src="`https://flagcdn.com/w640/${country.code.toLowerCase()}.png`"
          :alt="`Bandeira: ${country.name}`"
          class="aspect-3/2 w-full object-cover"
        />

        <div class="absolute inset-0 flex items-center justify-center bg-primary p-4 text-center text-tertiary text-2xl font-bold opacity-0 transition-opacity group-hover:opacity-100 lg:text-4xl">
          {{ country.name }}
        </div>
      </div>
    </div>
  </section>

  <section class="container my-8 lg:my-16">
    <h3 class="text-3xl font-bold">
      SOBRE
    </h3>

    <div class="grid grid-cols-1 items-center gap-8 my-8 lg:grid-cols-2 lg:gap-16">
      <img src="/main-image.svg" alt="imagens de pessoas com livro" class="h-72 mx-auto lg:h-150" />

      <div>
        <h4 class="text-3xl font-bold">Language Course</h4>
        <p class="text-xl font-medium lg:text-2xl">Aprenda inglês, conquiste novas oportunidades</p>

        <p class="text-lg my-6 lg:text-2xl lg:my-8">O Language Course é uma plataforma desenvolvida para brasileiros que desejam aprender inglês de forma acessível, prática e intuitiva. O objetivo é tornar o aprendizado de novas línguas mais simples e ajudar cada pessoa a ampliar seus horizontes, desenvolver novas habilidades e conquistar oportunidades pessoais e profissionais.</p>

        <p class="text-lg lg:text-2xl">A plataforma busca reunir recursos que incentivem o aprendizado contínuo, permitindo que os usuários desenvolvam seu vocabulário, aprimorem a compreensão e ganhem confiança na comunicação em inglês.
          Com foco nas necessidades dos brasileiros, o Language Course pretende aproximar o ensino de inglês da realidade de quem fala português, tornando a jornada de aprendizado mais familiar e motivadora.</p>

        <div class="flex flex-wrap gap-4 my-6 lg:gap-8 lg:my-8">
          <router-link class="btn btn-border" to="/documentacao">
            Documentação
          </router-link>

          <router-link class="btn btn-secondary" to="/login">
            Login
          </router-link>
        </div>
      </div>
    </div>
  </section>

  <ECFooter />
</template>
