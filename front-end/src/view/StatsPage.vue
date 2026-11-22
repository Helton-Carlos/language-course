<script lang="ts" setup>
import { Bookmark, BookOpen, CircleCheck, Flame, Repeat } from 'lucide-vue-next';
import { computed } from 'vue';
import ECPageHeader from '@/components/ECPageHeader/ECPageHeader.vue';
import ECCard from '@/components/ECCard/ECCard.vue';
import { useStats } from '@/composables/useStats';
import { formatWeekday } from '@/utils/dates';
import { MESSAGES } from '@/utils/message';
import { STATUS_BADGE_CLASSES, STATUS_LABELS } from '@/utils/words';

const { data: stats, isPending, isError } = useStats();

const maxDayTotal = computed(() =>
  Math.max(1, ...(stats.value?.last_days ?? []).map((day) => day.words_saved + day.reviews)),
);

const maxStatusCount = computed(() =>
  Math.max(1, ...(stats.value?.by_status ?? []).map((item) => item.count)),
);
</script>

<template>
  <section>
    <ECPageHeader
      :back-to="{ name: 'dashboard' }"
      title="Estatísticas"
      description="Seu progresso de estudo em inglês."
    />

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
          <ECCard width="100%">
            <template #body>
              <p class="flex items-center gap-2">
                <Bookmark class="h-5 w-5 text-primary" aria-hidden="true" />
                Palavras salvas
              </p>
              <p class="mt-1 text-2xl font-bold text-tertiary">
                {{ stats.total_items }}
              </p>
            </template>
          </ECCard>
        </li>
        <li>
          <ECCard width="100%">
            <template #body>
              <p class="flex items-center gap-2">
                <BookOpen class="h-5 w-5 text-primary" aria-hidden="true" />
                Palavras lidas
              </p>
              <p class="mt-1 text-2xl font-bold text-tertiary">
                {{ stats.words_read_total }}
              </p>
            </template>
          </ECCard>
        </li>
      </ul>

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
          <Repeat class="mr-1 inline h-5 w-5 align-text-bottom" aria-hidden="true" />
          Revisar agora
        </router-link>
      </div>
    </template>
  </section>
</template>
