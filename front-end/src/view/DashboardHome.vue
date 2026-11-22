<script lang="ts" setup>
import { CircleCheck, Flame, Repeat, Target } from 'lucide-vue-next';
import { computed } from 'vue';
import ECCard from '@/components/ECCard/ECCard.vue';
import ECFeatureCard from '@/components/ECFeatureCard/ECFeatureCard.vue';
import ECPageHeader from '@/components/ECPageHeader/ECPageHeader.vue';
import { useCurrentUser } from '@/composables/useCurrentUser';
import { useStats } from '@/composables/useStats';
import { CONTENTS } from '@/utils/contents';
import { SKILLS } from '@/utils/skills';
import { STUDY_AREAS } from '@/utils/study';

const { data: user } = useCurrentUser();
const { data: stats } = useStats();

const goalPercent = computed<number>(() => {
  if (!stats.value) return 0;
  return Math.min(100, Math.round((stats.value.today_progress / stats.value.daily_goal) * 100));
});

const goalReached = computed<boolean>(() => goalPercent.value >= 100);
</script>

<template>
  <section>
    <ECPageHeader title="Dashboard">
      <template v-if="user" #description>
        Bem-vindo de volta, <strong>{{ user.name }}</strong>.
      </template>
    </ECPageHeader>

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

    <section v-if="stats" class="mt-4 rounded-2xl bg-white p-5 shadow-sm" aria-labelledby="daily-goal-title">
      <div class="flex items-center justify-between gap-4">
        <h2 id="daily-goal-title" class="flex items-center gap-2 text-xl font-bold">
          <component :is="goalReached ? CircleCheck : Target" class="h-6 w-6 text-primary" aria-hidden="true" />
          Meta do dia
        </h2>
        <p class="text-quaternary">
          {{ stats.today_progress }} de {{ stats.daily_goal }}
        </p>
      </div>
      <div
        class="mt-3 h-3 overflow-hidden rounded-full bg-gray"
        role="progressbar"
        aria-label="Progresso da meta do dia"
        :aria-valuenow="goalPercent"
        aria-valuemin="0"
        aria-valuemax="100"
      >
        <div class="h-full bg-quinary transition-all" :style="{ width: `${goalPercent}%` }" />
      </div>
      <p class="mt-2 text-quaternary">
        {{ goalReached ? 'Meta concluída. Continue estudando para manter a sequência.' : 'Cada palavra salva e cada cartão revisado contam como um ponto.' }}
      </p>
    </section>    <ul v-if="stats" class="mt-4 grid gap-4 sm:grid-cols-3">
      <li>
        <ECCard width="100%">
          <template #body>
            <p class="flex items-center gap-2">
              <Flame class="h-5 w-5 text-primary" aria-hidden="true" />
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
            <p class="flex items-center gap-2">
              <CircleCheck class="h-5 w-5 text-primary" aria-hidden="true" />
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
              <p class="flex items-center gap-2">
                <Repeat class="h-5 w-5 text-primary" aria-hidden="true" />
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
      Estude seu vocabulário
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
