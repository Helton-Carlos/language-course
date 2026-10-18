<script lang="ts" setup>
import { ref } from 'vue';
import ECButton from '@/components/ECButton/ECButton.vue';
import ECInput from '@/components/ECInput/ECInput.vue';

const email = ref('');
const password = ref('');
</script>

<template>
  <div class="container flex justify-center my-8 lg:my-16">
    <form class="w-full max-w-180 flex flex-col gap-4 p-6 rounded-2xl bg-white shadow-md lg:p-8">
      <ECInput
        id="email"
        v-model="email"
        label="E-mail"
        type="email"
        placeholder="seuemail@exemplo.com"
      />
      <ECInput
        id="password"
        v-model="password"
        label="Senha"
        type="password"
        placeholder="Digite sua senha"
      />
      <ECButton type="submit" color="secondary">
        Entrar
      </ECButton>
    </form>
  </div>
</template>
