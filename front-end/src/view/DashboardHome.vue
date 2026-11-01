<script lang="ts" setup>
import ECCard from '@/components/ECCard/ECCard.vue';
import ECFeatureCard from '@/components/ECFeatureCard/ECFeatureCard.vue';
import { useCurrentUser } from '@/composables/useCurrentUser';
import { useLanguages } from '@/composables/useLanguages';
import { MESSAGES } from '@/utils/message';
import { CONTENTS } from '@/utils/contents';
import { SKILLS } from '@/utils/skills';

const { data: user } = useCurrentUser();
const { languages, isPending, isError } = useLanguages();
</script>

<template>
  <section>
    <h1 class="text-3xl font-bold">
      Dashboard
    </h1>

    <p v-if="user" class="mt-2 text-quaternary">
      Bem-vindo de volta, <strong>{{ user.name }}</strong>.
    </p>

    <ul v-if="user" class="mt-6 grid gap-4 sm:grid-cols-3">
      <li>
        <ECCard width="100%">
          <template #body>
            <p>
              Idioma
            </p>
            <p class="mt-1 flex items-center gap-3 text-2xl font-bold capitalize text-tertiary">
              <img
                v-if="user.language"
                :src="`https://flagcdn.com/${user.language.prefix.toLowerCase()}.svg`"
                :alt="`Bandeira: ${user.language.name_pt}`"
                class="h-6 w-9 rounded-sm object-cover"
              >
              {{ user.language?.name_pt ?? '-' }}
            </p>
          </template>
        </ECCard>
      </li>

      <li>
        <ECCard width="100%">
          <template #body>
            <p>
              Nível
            </p>
            <p class="mt-1 text-2xl font-bold text-tertiary">
              {{ user.level ?? '-' }}
            </p>
          </template>
        </ECCard>
      </li>
    </ul>

    <h2 class="mt-10 text-xl font-bold">
      Como você quer praticar?
    </h2>

    <ul class="mt-4 grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      <li v-for="skill in SKILLS" :key="skill.key">
        <ECFeatureCard
          :to="{ name: skill.routeName }"
          :title="skill.label"
          :description="skill.description"
          :icon="skill.icon"
        />
      </li>
    </ul>

    <h2 class="mt-10 text-xl font-bold">
      Explore conteúdos
    </h2>

    <ul class="mt-4 grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
      <li v-for="content in CONTENTS" :key="content.key">
        <ECFeatureCard
          :to="{ name: content.routeName }"
          :title="content.label"
          :description="content.description"
          :icon="content.icon"
        />
      </li>
    </ul>

    <h2 class="mt-10 text-xl font-bold">
      Trocar de idioma
    </h2>

    <p v-if="isPending" class="mt-4">
      {{ MESSAGES.pending.languagesLoad }}
    </p>

    <p v-else-if="isError" class="mt-4 text-red-700" role="alert">
      {{ MESSAGES.error.languagesLoad }}
    </p>

    <ul v-else class="mt-4 grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
      <li v-for="language in languages" :key="language.code">
        <router-link
          :to="{ name: 'escolher-nivel', params: { id: language.id } }"
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
            <p class="text-quaternary">
              {{ language.countries.length }} {{ language.countries.length === 1 ? 'país' : 'países' }}
            </p>
          </div>
        </router-link>
      </li>
    </ul>
  </section>
</template>
