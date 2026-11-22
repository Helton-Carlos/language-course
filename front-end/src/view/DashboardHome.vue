<script lang="ts" setup>
import ECCard from '@/components/ECCard/ECCard.vue';
import ECFeatureCard from '@/components/ECFeatureCard/ECFeatureCard.vue';
import { useCurrentUser } from '@/composables/useCurrentUser';
import { useStats } from '@/composables/useStats';
import { CONTENTS } from '@/utils/contents';
import { SKILLS } from '@/utils/skills';
import { STUDY_AREAS } from '@/utils/study';

const { data: user } = useCurrentUser();
const { data: stats } = useStats();
</script>

<template>
  <section>
    <h1 class="text-3xl font-bold">
      Dashboard
    </h1>

    <p v-if="user" class="mt-2 text-quaternary">
      Bem-vindo de volta, <strong>{{ user.name }}</strong>.
    </p>

    <ul v-if="user" class="mt-6 grid gap-4 sm:grid-cols-2">
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

    <ul v-if="stats" class="mt-4 grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      <li>
        <ECCard width="100%">
          <template #body>
            <p>
              Sequência
            </p>
            <p class="mt-1 text-2xl font-bold text-tertiary">
              {{ stats.streak }} {{ stats.streak === 1 ? 'dia' : 'dias' }}
            </p>
          </template>
        </ECCard>
      </li>
      <li>
        <ECCard width="100%">
          <template #body>
            <p>
              Meta de hoje
            </p>
            <p class="mt-1 text-2xl font-bold text-tertiary">
              {{ stats.today_progress }}/{{ stats.daily_goal }}
            </p>
          </template>
        </ECCard>
      </li>
      <li>
        <ECCard width="100%">
          <template #body>
            <p>
              Palavras conhecidas
            </p>
            <p class="mt-1 text-2xl font-bold text-tertiary">
              {{ stats.known_words }}
            </p>
          </template>
        </ECCard>
      </li>
      <li>
        <router-link :to="{ name: 'dashboard-revisar' }" class="block">
          <ECCard width="100%">
            <template #body>
              <p>
                Para revisar
              </p>
              <p class="mt-1 text-2xl font-bold text-tertiary">
                {{ stats.due_count }}
              </p>
            </template>
          </ECCard>
        </router-link>
      </li>
    </ul>
    <h2 class="mt-10 text-xl font-bold">
      Estude com LingQs
    </h2>
    <ul class="mt-4 grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      <li v-for="area in STUDY_AREAS" :key="area.key">
        <ECFeatureCard
          :to="{ name: area.routeName }"
          :title="area.label"
          :description="area.description"
          :icon="area.icon"
        />
      </li>
    </ul>    <h2 class="mt-10 text-xl font-bold">
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
  </section>
</template>
