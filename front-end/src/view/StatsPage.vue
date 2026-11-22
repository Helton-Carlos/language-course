<script lang="ts" setup>
import { computed } from 'vue';
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import ECCard from '@/components/ECCard/ECCard.vue';
import { useStats } from '@/composables/useStats';
import { formatWeekday } from '@/utils/dates';
import { MESSAGES } from '@/utils/message';
import { STATUS_BADGE_CLASSES, STATUS_LABELS } from '@/utils/words';

const { data: stats, isPending, isError } = useStats();

const goalPercent = computed(() => {
  if (!stats.value) return 0;
  return Math.min(100, Math.round((stats.value.today_progress / stats.value.daily_goal) * 100));
});

const maxDayTotal = computed(() =>
  Math.max(1, ...(stats.value?.last_days ?? []).map((day) => day.words_saved + day.reviews)),
);

const maxStatusCount = computed(() =>
  Math.max(1, ...(stats.value?.by_status ?? []).map((item) => item.count)),
);
</script>

<template>
  <section>
    <ECBackButton :to="{ name: 'dashboard' }" />
    <h1 class="mt-4 text-3xl font-bold">
      Estatísticas
    </h1>
    <p class="mt-2 text-quaternary">
      Seu progresso de estudo em inglês.
    </p>

    <p v-if="isPending" class="mt-6">
      {{ MESSAGES.pending.statsLoad }}
    </p>
    <p v-else-if="isError" class="mt-6 text-red-700" role="alert">
      {{ MESSAGES.error.statsLoad }}
    </p>

    <template v-else-if="stats">
      <ul class="mt-6 grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
        <li>
          <ECCard width="100%">
            <template #body>
              <p>Sequência</p>
              <p class="mt-1 text-2xl font-bold text-tertiary">
                {{ stats.streak }} {{ stats.streak === 1 ? 'dia' : 'dias' }}
              </p>
            </template>
          </ECCard>
        </li>
        <li>
          <ECCard width="100%">
            <template #body>
              <p>Palavras conhecidas</p>
              <p class="mt-1 text-2xl font-bold text-tertiary">
                {{ stats.known_words }}
              </p>
            </template>
          </ECCard>
        </li>
        <li>
          <ECCard width="100%">
            <template #body>
              <p>Palavras salvas</p>
              <p class="mt-1 text-2xl font-bold text-tertiary">
                {{ stats.total_items }}
              </p>
            </template>
          </ECCard>
        </li>
        <li>
          <ECCard width="100%">
            <template #body>
              <p>Palavras lidas</p>
              <p class="mt-1 text-2xl font-bold text-tertiary">
                {{ stats.words_read_total }}
              </p>
            </template>
          </ECCard>
        </li>
      </ul>

      <div class="mt-8 rounded-2xl bg-white p-5 shadow-sm">
        <div class="flex items-center justify-between">
          <h2 class="text-xl font-bold">
            Meta de hoje
          </h2>
          <p class="text-quaternary">
            {{ stats.today_progress }} de {{ stats.daily_goal }}
          </p>
        </div>
        <div
          class="mt-3 h-3 overflow-hidden rounded-full bg-gray"
          role="progressbar"
          aria-label="Progresso da meta diária"
          :aria-valuenow="goalPercent"
          aria-valuemin="0"
          aria-valuemax="100"
        >
          <div class="h-full bg-quinary transition-all" :style="{ width: `${goalPercent}%` }" />
        </div>
        <p class="mt-2 text-quaternary">
          Cada palavra salva e cada cartão revisado contam como um ponto.
        </p>
      </div>

      <div class="mt-6 grid gap-6 lg:grid-cols-2">
        <div class="rounded-2xl bg-white p-5 shadow-sm">
          <h2 class="text-xl font-bold">
            Últimos 7 dias
          </h2>
          <ul class="mt-4 flex h-40 items-end gap-2">
            <li v-for="day in stats.last_days" :key="day.day" class="flex h-full flex-1 flex-col items-center justify-end gap-1">
              <span class="text-quaternary">{{ day.words_saved + day.reviews }}</span>
              <div
                class="w-full rounded-t bg-primary"
                :style="{ height: `${((day.words_saved + day.reviews) / maxDayTotal) * 100}%`, minHeight: '2px' }"
                :title="`${day.words_saved} salvas, ${day.reviews} revisões, ${day.words_read} palavras lidas`"
              />
              <span class="capitalize text-quaternary">{{ formatWeekday(day.day) }}</span>
            </li>
          </ul>
        </div>

        <div class="rounded-2xl bg-white p-5 shadow-sm">
          <h2 class="text-xl font-bold">
            Vocabulário por nível
          </h2>
          <ul class="mt-4 flex flex-col gap-3">
            <li v-for="item in stats.by_status" :key="item.status" class="grid grid-cols-[6.5rem_1fr_2.5rem] items-center gap-3">
              <span class="text-quaternary">{{ STATUS_LABELS[item.status] }}</span>
              <div class="h-3 overflow-hidden rounded-full bg-gray">
                <div
                  :class="['h-full', STATUS_BADGE_CLASSES[item.status]]"
                  :style="{ width: `${(item.count / maxStatusCount) * 100}%` }"
                />
              </div>
              <span class="text-right font-medium text-tertiary">{{ item.count }}</span>
            </li>
          </ul>
        </div>
      </div>

      <div v-if="stats.due_count" class="mt-6 rounded-2xl bg-white p-5 shadow-sm">
        <p class="font-medium text-tertiary">
          Você tem {{ stats.due_count }} {{ stats.due_count === 1 ? 'cartão' : 'cartões' }} para revisar.
        </p>
        <router-link :to="{ name: 'dashboard-revisar' }" class="btn btn-secondary mt-3 inline-block">
          Revisar agora
        </router-link>
      </div>
    </template>
  </section>
</template>
