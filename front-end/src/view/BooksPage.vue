<script lang="ts" setup>
import ECPageHeader from '@/components/ECPageHeader/ECPageHeader.vue';
import ECFeatureCard from '@/components/ECFeatureCard/ECFeatureCard.vue';
import { BOOK_THEMES } from '@/utils/bookThemes';
</script>

<template>
  <section>
    <ECPageHeader
      :back-to="{ name: 'dashboard' }"
      title="Ler um livro"
      description="Escolha um tema para ver os livros disponíveis."
    />

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
