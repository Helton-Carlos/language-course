<script lang="ts" setup>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import ECCard from '@/components/ECCard/ECCard.vue';
import { hasCompleteProfile, useCurrentUser } from '@/composables/useCurrentUser';
import { useLanguages } from '@/composables/useLanguages';
import { MESSAGES } from '@/utils/message';

const router = useRouter();
const { data: user } = useCurrentUser();
const { languages, isPending, isError } = useLanguages();

const backTo = computed(() =>
  user.value && hasCompleteProfile(user.value) ? { name: 'dashboard' } : { name: 'index' },
);

function choose(id: string) {
  router.push({ name: 'escolher-nivel', params: { id } });
}
</script>

<template>
  <section>
    <ECBackButton :to="backTo" />

    <h1 class="mt-4 text-3xl font-bold">
      Olá<template v-if="user">, {{ user.name }}</template>!
    </h1>

    <p class="mt-2 text-xl text-quaternary">
      Qual idioma você quer aprender?
    </p>

    <p v-if="isPending" class="mt-6">
      {{ MESSAGES.pending.languagesLoad }}
    </p>

    <p v-else-if="isError" class="mt-6 text-red-700" role="alert">
      {{ MESSAGES.error.languagesLoad }}
    </p>

    <ul v-else class="mt-6 grid gap-6 sm:grid-cols-2 xl:grid-cols-3">
      <li v-for="language in languages" :key="language.code">
        <ECCard
          class="flex h-full flex-col"
          width="100%"
          clickable
          @on-click="choose(language.id)"
        >
          <template #body>
            <div class="flex h-full flex-col">
              <div class="flex items-center gap-4">
                <img
                  :src="`https://flagcdn.com/${language.prefix.toLowerCase()}.svg`"
                  :alt="`Bandeira: ${language.name_pt}`"
                  class="h-10 w-16 rounded-sm object-cover"
                >

                <div>
                  <h2 class="text-2xl font-bold capitalize text-tertiary">
                    {{ language.name_pt }}
                  </h2>
                  <p>
                    {{ language.name }}
                  </p>
                </div>
              </div>

              <p class="mt-4">
                {{ language.description }}
              </p>

              <p class="mt-auto pt-4 font-medium text-tertiary">
                Falado em: {{ language.countries.join(', ') }}
              </p>
            </div>
          </template>
        </ECCard>
      </li>
    </ul>
  </section>
</template>
