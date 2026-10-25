<script lang="ts" setup>
import { storeToRefs } from 'pinia';
import { useRouter } from 'vue-router';
import { languagesStore } from '@/stores/languages.ts';

import ECButton from '@/components/ECButton/ECButton.vue';

interface DocStep {
  title: string;
  description: string;
}

const router = useRouter();
const store = languagesStore();
const { languages } = storeToRefs(store);

function goHome() {
  router.push({ name: 'index' });
}

const steps: DocStep[] = [
  {
    title: 'Escolha o idioma',
    description: 'Na página inicial, veja os idiomas disponíveis e clique no que você quer aprender.',
  },
  {
    title: 'Defina um objetivo',
    description: 'Viagem, trabalho, estudos ou lazer. Saber por que você estuda ajuda a escolher o que praticar primeiro.',
  },
  {
    title: 'Comece pelo básico',
    description: 'Cumprimentos, apresentações, números e frases do dia a dia dão confiança logo nas primeiras semanas.',
  },
  {
    title: 'Pratique todos os dias',
    description: 'Poucos minutos por dia rendem mais do que uma sessão longa uma vez por semana.',
  },
  {
    title: 'Revise o que aprendeu',
    description: 'Volte ao vocabulário antigo com frequência. Revisar em intervalos ajuda a fixar na memória.',
  },
];

const skills: DocStep[] = [
  {
    title: 'Vocabulário',
    description: 'Aprenda palavras em contexto, dentro de frases, e não só listas soltas. Use as palavras novas logo que aprender.',
  },
  {
    title: 'Escuta',
    description: 'Ouça músicas, vídeos e podcasts no idioma. No início, não precisa entender tudo: foque em captar o sentido geral.',
  },
  {
    title: 'Fala',
    description: 'Repita frases em voz alta e imite a pronúncia. Errar faz parte e é a forma mais rápida de melhorar.',
  },
  {
    title: 'Leitura',
    description: 'Comece com textos curtos e simples. Sublinhe as palavras novas e releia depois.',
  },
  {
    title: 'Escrita',
    description: 'Escreva frases sobre o seu dia, anote o que aprendeu e tente contar pequenas histórias.',
  },
];

const routine: DocStep[] = [
  { title: '5 minutos', description: 'Revise o vocabulário do dia anterior.' },
  { title: '10 minutos', description: 'Aprenda um conteúdo novo, como palavras ou uma estrutura de frase.' },
  { title: '5 minutos', description: 'Pratique em voz alta ou escreva três frases usando o que aprendeu.' },
];

const tips: string[] = [
  'Não tenha medo de errar. Todo mundo que aprende um idioma comete erros no começo.',
  'Compare o novo idioma com o português para entender semelhanças e diferenças.',
  'Cerque-se do idioma: mude o idioma do celular, assista séries e siga perfis na língua que você estuda.',
  'Defina metas pequenas, como aprender 5 palavras por dia, e comemore cada conquista.',
  'Seja constante. Faltar um dia não é problema, o importante é voltar no dia seguinte.',
];
</script>

<template>
  <div class="container my-8 flex flex-col gap-8 lg:my-16">
    <div>
      <h1 class="text-4xl font-bold lg:text-6xl">
        Como aprender um idioma
      </h1>
      <p class="my-4 text-xl lg:text-2xl">
        O Language Course ajuda você a aprender novos idiomas de forma simples e prática.
        Veja abaixo como começar e como manter o ritmo.
      </p>
    </div>

    <section class="flex flex-col gap-4">
      <h2 class="text-3xl font-bold">
        Passo a passo
      </h2>
      <ol class="grid grid-cols-1 gap-4 md:grid-cols-2">
        <li
          v-for="(step, index) in steps"
          :key="step.title"
          class="rounded-lg bg-white p-4 shadow-sm"
        >
          <span class="text-quaternary">Passo {{ index + 1 }}</span>
          <h3 class="text-xl font-bold">
            {{ step.title }}
          </h3>
          <p class="text-quaternary">
            {{ step.description }}
          </p>
        </li>
      </ol>
    </section>

    <section class="flex flex-col gap-4">
      <h2 class="text-3xl font-bold">
        Idiomas disponíveis
      </h2>
      <ul class="flex flex-wrap gap-4 rounded-2xl bg-white p-4 shadow-sm">
        <li
          v-for="language in languages"
          :key="language.code"
          class="flex items-center gap-3"
        >
          <img
            :src="`https://flagcdn.com/${language.prefix.toLowerCase()}.svg`"
            :alt="`Bandeira: ${language.name_pt}`"
            class="h-5 w-8 rounded-sm object-cover"
          />
          <span class="capitalize">{{ language.name_pt }}</span>
        </li>
      </ul>
    </section>

    <section class="flex flex-col gap-4">
      <h2 class="text-3xl font-bold">
        Desenvolva as 5 habilidades
      </h2>
      <ul class="grid grid-cols-1 gap-4 md:grid-cols-2">
        <li
          v-for="skill in skills"
          :key="skill.title"
          class="rounded-lg bg-white p-4 shadow-sm"
        >
          <h3 class="text-xl font-bold">
            {{ skill.title }}
          </h3>
          <p class="text-quaternary">
            {{ skill.description }}
          </p>
        </li>
      </ul>
    </section>

    <section class="flex flex-col gap-4">
      <h2 class="text-3xl font-bold">
        Rotina sugerida: 20 minutos por dia
      </h2>
      <ul class="grid grid-cols-1 gap-4 md:grid-cols-3">
        <li
          v-for="item in routine"
          :key="item.description"
          class="rounded-lg bg-primary p-4 text-tertiary"
        >
          <h3 class="text-xl font-bold">
            {{ item.title }}
          </h3>
          <p>{{ item.description }}</p>
        </li>
      </ul>
    </section>

    <section class="flex flex-col gap-4">
      <h2 class="text-3xl font-bold">
        Dicas para não desistir
      </h2>
      <ul class="flex list-disc flex-col gap-2 pl-6">
        <li
          v-for="tip in tips"
          :key="tip"
        >
          {{ tip }}
        </li>
      </ul>
    </section>

    <div class="flex">
      <ECButton color="secondary" @onClick="goHome">
        Escolher meu idioma
      </ECButton>
    </div>
  </div>
</template>
