<script lang="ts" setup>
import { useRouter } from 'vue-router';
import ECCard from '@/components/ECCard/ECCard.vue';
import ECFooter from '@/layouts/ECFooter.vue';
import { useCurrentUser } from '@/composables/useCurrentUser';
import { useLanguages } from '@/composables/useLanguages';
import { MESSAGES } from '@/utils/message';

const router = useRouter();
const { data: user } = useCurrentUser();
const { languages, isPending, isError } = useLanguages();

function choose(id: string) {
  router.push({ name: 'escolher-nivel', params: { id } });
}
</script>

<template>
  <div class="flex min-h-full flex-col">
    <div class="flex-1">
      <div class="container my-8 lg:my-16">
        <h1 class="text-4xl font-bold lg:text-5xl">
          Olá<template v-if="user">, {{ user.name }}</template>!
        </h1>

        <p class="mt-4 text-2xl">
          Qual idioma você quer aprender?
        </p>

        <p v-if="isPending" class="mt-8">
          {{ MESSAGES.pending.languagesLoad }}
        </p>

        <p v-else-if="isError" class="mt-8 text-red-700" role="alert">
          {{ MESSAGES.error.languagesLoad }}
        </p>

        <ul v-else class="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
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
                      <p class="text-sm">
                        {{ language.name }}
                      </p>
                    </div>
                  </div>

                  <p class="mt-4 text-sm">
                    {{ language.description }}
                  </p>

                  <p class="mt-auto pt-4 text-sm font-medium text-tertiary">
                    Falado em: {{ language.countries.join(', ') }}
                  </p>
                </div>
              </template>
            </ECCard>
          </li>
        </ul>
      </div>
    </div>

    <ECFooter />
  </div>
</template>
