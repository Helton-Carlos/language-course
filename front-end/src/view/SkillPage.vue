<script lang="ts" setup>
import ECPageHeader from '@/components/ECPageHeader/ECPageHeader.vue';
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
    <ECPageHeader
      :back-to="{ name: 'dashboard' }"
      :title="skill.label"
      :description="skill.description"
      :icon="skill.icon"
    />

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
