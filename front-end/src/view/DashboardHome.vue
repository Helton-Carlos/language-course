<script lang="ts" setup>
import { computed } from 'vue';
import ECCard from '@/components/ECCard/ECCard.vue';
import { useLanguages } from '@/composables/useLanguages';
import { LEVELS } from '@/utils/levels';
import { MESSAGES } from '@/utils/message';

interface InfoCard {
  key: string;
  label: string;
  value: string | number;
  hint: string;
}

const { languages, isPending, isError } = useLanguages();

const infoCards = computed<InfoCard[]>(() => {
  const countries = new Set(languages.value.flatMap((language) => language.countries));

  const widest = languages.value.reduce<(typeof languages.value)[number] | null>(
    (best, language) =>
      best === null || language.countries.length > best.countries.length ? language : best,
    null,
  );

  return [
    {
      key: 'languages',
      label: 'Idiomas disponíveis',
      value: languages.value.length,
      hint: 'Cadastrados na plataforma',
    },
    {
      key: 'countries',
      label: 'Países diferentes',
      value: countries.size,
      hint: 'Onde esses idiomas são falados',
    },
    {
      key: 'widest',
      label: 'Maior alcance',
      value: widest?.name_pt ?? '-',
      hint: widest ? `Usado em ${widest.countries.length} países` : 'Sem dados',
    },
    {
      key: 'levels',
      label: 'Níveis',
      value: `${LEVELS[0]} a ${LEVELS[LEVELS.length - 1]}`,
      hint: `${LEVELS.length} níveis de proficiência`,
    },
  ];
});
</script>

<template>
  <section>
    <h1 class="text-3xl font-bold">
      Dashboard
    </h1>

    <p class="mt-2 text-quaternary">
      Escolha um idioma para começar ou use o menu ao lado.
    </p>

    <p v-if="isPending" class="mt-6">
      {{ MESSAGES.pending.languagesLoad }}
    </p>

    <p v-else-if="isError" class="mt-6 text-red-700" role="alert">
      {{ MESSAGES.error.languagesLoad }}
    </p>

    <template v-else>
      <ul class="mt-6 grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
        <li v-for="card in infoCards" :key="card.key">
          <ECCard width="100%">
            <template #body>
              <p class="text-sm">
                {{ card.label }}
              </p>
              <p class="mt-1 text-3xl font-bold capitalize text-tertiary">
                {{ card.value }}
              </p>
              <p class="mt-1 text-xs">
                {{ card.hint }}
              </p>
            </template>
          </ECCard>
        </li>
      </ul>

      <h2 class="mt-10 text-xl font-bold">
        Idiomas
      </h2>

      <ul class="mt-4 grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
        <li v-for="language in languages" :key="language.code">
          <router-link
            :to="{ name: 'dashboard-idioma', params: { id: language.id } }"
            class="flex items-center gap-4 rounded-2xl bg-white p-4 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"
          >
            <img
              :src="`https://flagcdn.com/${language.prefix.toLowerCase()}.svg`"
              :alt="`Bandeira: ${language.name_pt}`"
              class="h-8 w-12 rounded-sm object-cover"
            >

            <div>
              <p class="font-bold capitalize">
                {{ language.name_pt }}
              </p>
              <p class="text-sm text-quaternary">
                {{ language.countries.length }} {{ language.countries.length === 1 ? 'país' : 'países' }}
              </p>
            </div>
          </router-link>
        </li>
      </ul>
    </template>
  </section>
</template>
