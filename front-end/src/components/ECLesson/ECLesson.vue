<script setup lang="ts">
import { CircleCheck } from 'lucide-vue-next';
import { toRef } from 'vue';
import ECButton from '@/components/ECButton/ECButton.vue';
import ECReader from '@/components/ECReader/ECReader.vue';
import type { ECLesson } from '@/components/ECLesson/Type';
import { useCompleteLesson } from '@/composables/useCompleteLesson';
import { countWords } from '@/utils/words';

const props = defineProps<ECLesson>();

const { unknownTerms, isCompleting, complete } = useCompleteLesson(toRef(props, 'body'));
</script>

<template>
  <div>
    <h1 class="mt-4 text-3xl font-bold">
      {{ title }}
    </h1>
    <p class="mt-1 text-quaternary">
      {{ countWords(body) }} palavras
    </p>
    <div class="mt-6">
      <ECReader :body="body" />
    </div>
    <div class="mt-8 flex flex-wrap items-center gap-4">
      <ECButton color="secondary" :disabled="isCompleting" @on-click="complete">
        <CircleCheck class="mr-1 inline h-5 w-5 align-text-bottom" aria-hidden="true" />
        Concluir lição
      </ECButton>
      <p class="text-quaternary">
        <template v-if="unknownTerms.length">
          {{ unknownTerms.length }} palavras azuis serão marcadas como conhecidas.
        </template>
        <template v-else>
          Todas as palavras deste texto já estão no seu vocabulário.
        </template>
      </p>
    </div>
  </div>
</template>
