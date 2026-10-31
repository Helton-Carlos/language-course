<script lang="ts" setup>
import { languagesStore } from '@/stores/languages.ts'
import { storeToRefs } from 'pinia';

const store = languagesStore()
const { languages } = storeToRefs(store)

</script>

<template>
  <div class="container">
    <h3 class="text-3xl font-bold mt-16">
      IDIOMAS
    </h3>

    <div class="grid gap-6 my-8 md:grid-cols-2 lg:grid-cols-3">
      <article
        v-for="language in languages"
        :key="language.code"
        class="rounded-lg bg-white p-6 shadow-sm"
      >
        <div class="flex items-center gap-3">
          <img
            :src="`https://flagcdn.com/${language.prefix.toLowerCase()}.svg`"
            :alt="`Bandeira: ${language.name_pt}`"
            class="h-6 w-9 rounded-sm object-cover"
          />

          <h4 class="text-2xl font-bold capitalize">
            {{ language.name_pt }}
            <span class="text-base font-normal text-quaternary">({{ language.name }})</span>
          </h4>
        </div>

        <p class="mt-4 text-quaternary">
          {{ language.description }}
        </p>

        <h5 class="mt-4 font-bold">
          Países que usam
        </h5>

        <ul class="mt-2 flex flex-wrap gap-2">
          <li
            v-for="country in language.countries"
            :key="country"
            class="rounded-full bg-primary px-3 py-1 text-sm text-tertiary"
          >
            {{ country }}
          </li>
        </ul>
      </article>
    </div>
  </div>
</template>
