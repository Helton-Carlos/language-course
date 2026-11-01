<script lang="ts" setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { useCurrentUser } from '@/composables/useCurrentUser';
import { SKILLS } from '@/utils/skills';

const route = useRoute();
const { data: user } = useCurrentUser();

const skill = computed(() => SKILLS.find((item) => item.key === route.meta.skill));
</script>

<template>
  <section v-if="skill">
    <router-link class="text-quaternary underline" :to="{ name: 'dashboard' }">
      Voltar ao dashboard
    </router-link>

    <div class="mt-4 flex items-center gap-4">
      <svg
        viewBox="0 0 24 24"
        fill="currentColor"
        class="h-10 w-10 text-secondary"
        aria-hidden="true"
      >
        <path :d="skill.icon" />
      </svg>

      <h1 class="text-3xl font-bold">
        {{ skill.label }}
      </h1>
    </div>

    <p class="mt-2 text-quaternary">
      {{ skill.description }}
    </p>

    <p v-if="user?.language && user.level" class="mt-6">
      Praticando
      <strong class="capitalize">{{ user.language.name_pt }}</strong>
      no nível
      <strong>{{ user.level }}</strong>.
    </p>

    <div class="mt-6 rounded-2xl bg-white p-6 shadow-sm">
      <p class="font-medium text-tertiary">
        Em breve
      </p>
      <p class="mt-1 text-quaternary">
        Os exercícios desta habilidade ainda estão sendo preparados.
      </p>
    </div>
  </section>
</template>
