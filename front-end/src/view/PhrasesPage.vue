<script lang="ts" setup>
import ECPageHeader from '@/components/ECPageHeader/ECPageHeader.vue';
import { computed } from 'vue';
import { useCurrentUser } from '@/composables/useCurrentUser';
import { usePhrases } from '@/composables/useContent';
import { MESSAGES } from '@/utils/message';
import type { PhraseKind } from '@/types/content';

const { data: user } = useCurrentUser();
const languageId = computed(() => user.value?.language_id);
const { data: phrases, isPending, isError } = usePhrases(languageId);

const groups = computed<{ kind: PhraseKind; title: string }[]>(() => [
  { kind: 'phrase', title: 'Frases' },
  { kind: 'slang', title: 'Gírias' },
]);

function byKind(kind: PhraseKind) {
  return (phrases.value ?? []).filter((phrase) => phrase.kind === kind);
}
</script>

<template>
  <section>
    <ECPageHeader
      :back-to="{ name: 'dashboard' }"
      title="Frases e gírias"
    >
      <template #description>
        Expressões em
        <span class="capitalize">{{ user?.language?.name_pt }}</span>
        com a tradução logo abaixo.
      </template>
    </ECPageHeader>

    <p v-if="isPending" class="mt-6">
      {{ MESSAGES.pending.phrasesLoad }}
    </p>

    <p v-else-if="isError" class="mt-6 text-red-700" role="alert">
      {{ MESSAGES.error.phrasesLoad }}
    </p>

    <template v-else>
      <div v-for="group in groups" :key="group.kind" class="mt-8">
        <h2 class="text-xl font-bold">
          {{ group.title }}
        </h2>

        <ul class="mt-4 grid gap-4 md:grid-cols-2">
          <li
            v-for="phrase in byKind(group.kind)"
            :key="phrase.id"
            class="rounded-2xl bg-white p-5 shadow-sm"
          >
            <p class="text-lg font-bold text-tertiary">
              {{ phrase.text }}
            </p>
            <p class="mt-1 text-quaternary">
              {{ phrase.translation }}
            </p>
          </li>
        </ul>
      </div>
    </template>
  </section>
</template>
