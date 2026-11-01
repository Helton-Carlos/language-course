<script lang="ts" setup>
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import { computed } from 'vue';
import { useCurrentUser } from '@/composables/useCurrentUser';
import { usePodcasts } from '@/composables/useContent';
import { MESSAGES } from '@/utils/message';

const { data: user } = useCurrentUser();
const languageId = computed(() => user.value?.language_id);
const { data: episodes, isPending, isError } = usePodcasts(languageId);
</script>

<template>
  <section>
    <ECBackButton :to="{ name: 'dashboard' }" />

    <h1 class="mt-4 text-3xl font-bold">
      Podcast
    </h1>

    <p class="mt-2 text-quaternary">
      Conversas reais em
      <span class="capitalize">{{ user?.language?.name_pt }}</span>
      para treinar a escuta.
    </p>

    <p v-if="isPending" class="mt-6">
      {{ MESSAGES.pending.podcastsLoad }}
    </p>

    <p v-else-if="isError" class="mt-6 text-red-700" role="alert">
      {{ MESSAGES.error.podcastsLoad }}
    </p>

    <ul v-else class="mt-6 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
      <li v-for="episode in episodes" :key="episode.id">
        <figure class="overflow-hidden rounded-2xl bg-white shadow-sm">
          <div class="aspect-video bg-black">
            <iframe
              class="h-full w-full"
              :src="`https://www.youtube-nocookie.com/embed/${encodeURIComponent(episode.youtube_id)}`"
              :title="episode.title"
              loading="lazy"
              referrerpolicy="strict-origin-when-cross-origin"
              allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share"
              allowfullscreen
            />
          </div>

          <figcaption class="p-4 font-medium text-tertiary">
            {{ episode.title }}
          </figcaption>
        </figure>
      </li>
    </ul>
  </section>
</template>
