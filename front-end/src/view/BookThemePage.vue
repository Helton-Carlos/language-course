<script lang="ts" setup>
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { useCurrentUser } from '@/composables/useCurrentUser';
import { BOOK_THEMES } from '@/utils/bookThemes';

const route = useRoute();
const { data: user } = useCurrentUser();

const theme = computed(() => BOOK_THEMES.find((item) => item.key === route.params.tema));
</script>

<template>
  <section v-if="theme">
    <ECBackButton :to="{ name: 'dashboard-livros' }" />

    <h1 class="mt-4 text-3xl font-bold">
      Livros: {{ theme.label }}
    </h1>

    <p class="mt-2 text-quaternary">
      {{ theme.description }}
    </p>

    <p v-if="user?.language && user.level" class="mt-6">
      Lendo em
      <strong class="capitalize">{{ user.language.name_pt }}</strong>
      no nível
      <strong>{{ user.level }}</strong>.
    </p>

    <div class="mt-6 rounded-2xl bg-white p-6 shadow-sm">
      <p class="font-medium text-tertiary">
        Em breve
      </p>
      <p class="mt-1 text-quaternary">
        Os livros deste tema ainda estão sendo selecionados.
      </p>
    </div>
  </section>
</template>
