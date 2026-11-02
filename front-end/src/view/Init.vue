<script lang="ts" setup>
import { computed, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import ECButton from '@/components/ECButton/ECButton.vue';
import { hasCompleteProfile, useCurrentUser } from '@/composables/useCurrentUser';
import { useEnglish } from '@/composables/useEnglish';
import { useSaveProfile } from '@/composables/useProfile';
import { LEVELS, isLevel, type Level } from '@/utils/levels';

const route = useRoute();
const router = useRouter();
const { data: user } = useCurrentUser();
const { english } = useEnglish();
const { mutate: saveProfile, isPending: isSaving } = useSaveProfile();

const queryLevel = route.query.level;
const selectedLevel = ref<Level>(isLevel(queryLevel) ? queryLevel : LEVELS[0]);

const backTo = computed(() =>
  user.value && hasCompleteProfile(user.value) ? { name: 'dashboard' } : { name: 'index' },
);

function goToTest() {
  router.push({ name: 'dashboard-teste-nivel' });
}

function confirmLevel() {
  saveProfile(
    { level: selectedLevel.value },
    { onSuccess: () => router.push({ name: 'dashboard' }) },
  );
}
</script>

<template>
  <div class="grid gap-10 lg:grid-cols-2">
    <div>
      <h2 class="text-4xl lg:text-5xl">
        Ótima escolha o
        <span class="relative inline-block">
          <span class="uppercase font-bold">{{ english?.name_pt }}</span>,
          <img
            src="/icon-risk.svg"
            alt="risco ilustrativo"
            class="pointer-events-none absolute bottom-full left-full w-[1.1em] translate-y-[0.15em]"
          >
        </span>
        <br>é utilizado em diversos países
        <br>ao redor do mundo.
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

        <ECButton color="border" :disabled="isSaving" @on-click="confirmLevel">
          Avançar
        </ECButton>
      </div>

      <p class="mt-8 text-2xl">
        Não sei meu nível?
      </p>

      <div class="mt-2 flex gap-4">
        <ECBackButton variant="button" :to="backTo" />

        <ECButton color="secondary" @on-click="goToTest">
          Teste
        </ECButton>
      </div>
    </div>

    <figure class="w-full max-w-sm justify-self-end rounded-lg bg-[#d9d9d9] p-5">
      <img
        :src="`https://flagcdn.com/${english?.prefix?.toLowerCase()}.svg`"
        :alt="`Bandeira: ${english?.name_pt}`"
        class="aspect-3/2 w-full object-cover"
      />

      <figcaption class="mt-3 text-xs">
        {{ english?.name_pt }}, {{ english?.prefix }}
      </figcaption>
    </figure>
  </div>
</template>
