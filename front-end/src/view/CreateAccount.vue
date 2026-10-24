<script lang="ts" setup>
import { reactive } from 'vue';
import ECButton from '@/components/ECButton/ECButton.vue';
import ECInput from '@/components/ECInput/ECInput.vue';

import type { accountForm } from '@/types/accountForm'

const form = reactive<accountForm>({
  name: '',
  email: '',
  password: '',
  passwordConfirm: '',
});
</script>

<template>
  <div class="container flex justify-center my-8 lg:my-16">
    <form class="w-full max-w-120 flex flex-col gap-4 p-6 rounded-2xl bg-white shadow-md lg:p-8">
      <ECInput
        id="name"
        v-model="form.name"
        label="Nome"
        type="text"
        placeholder="John Doe"
      />

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

      <ECInput
        id="password-confirm"
        v-model="form.passwordConfirm"
        label="Confirmar senha"
        type="password"
        placeholder="Digite sua senha"
      />

      <ECButton type="submit" color="secondary">
        Salvar
      </ECButton>

      <div class="flex items-center gap-4 text-quaternary">
        <span class="h-px flex-1 bg-black" />
        <span>ou</span>
        <span class="h-px flex-1 bg-black" />
      </div>

      <ECButton color="border">
        <span class="flex items-center justify-center gap-3">
          <img src="/google-logo.svg" />
          Cadastrar com Google
        </span>
      </ECButton>

      <router-link class="btn btn-border text-center" to="/login">
        Voltar
      </router-link>
    </form>
  </div>
</template>
