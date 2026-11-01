<script lang="ts" setup>
import ECFeatureCard from '@/components/ECFeatureCard/ECFeatureCard.vue';
import { BOOK_THEMES } from '@/utils/bookThemes';
</script>

<template>
  <section>
    <router-link class="text-quaternary underline" :to="{ name: 'dashboard' }">
      Voltar ao dashboard
    </router-link>

    <h1 class="mt-4 text-3xl font-bold">
      Ler um livro
    </h1>

    <p class="mt-2 text-quaternary">
      Escolha um tema para ver os livros disponíveis.
    </p>

    <ul class="mt-6 grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
      <li v-for="theme in BOOK_THEMES" :key="theme.key">
        <ECFeatureCard
          :to="{ name: 'dashboard-livros-tema', params: { tema: theme.key } }"
          :title="theme.label"
          :description="theme.description"
        />
      </li>
    </ul>
  </section>
</template>
