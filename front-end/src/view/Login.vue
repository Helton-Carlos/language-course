<script lang="ts" setup>
import { reactive } from 'vue';
import ECButton from '@/components/ECButton/ECButton.vue';
import ECInput from '@/components/ECInput/ECInput.vue';

import type { accountForm } from '@/types/accountForm'

const form = reactive<accountForm>({
  email: '',
  password: '',
});
</script>

<template>
  <div class="container flex justify-center my-8 lg:my-16">
    <form class="w-full max-w-120 flex flex-col gap-4 p-6 rounded-2xl bg-white shadow-md lg:p-8">
      <ECInput
        id="email"
        v-model="form.email"
        label="E-mail"
        type="email"
        placeholder="seuemail@exemplo.com"
      />

      <ECInput
        id="password"
        v-model="form.password"
        label="Senha"
        type="password"
        placeholder="Digite sua senha"
      />

      <ECButton type="submit" color="secondary">
        Entrar
      </ECButton>

      <router-link class="btn btn-border text-center" to="/criar-conta">
        Criar conta
      </router-link>
    </form>
  </div>
</template>
