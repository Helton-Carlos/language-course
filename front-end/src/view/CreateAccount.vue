<script lang="ts" setup>
import { reactive } from 'vue';
import { useRouter } from 'vue-router';
import ECButton from '@/components/ECButton/ECButton.vue';
import ECInput from '@/components/ECInput/ECInput.vue';
import { useRegister } from '@/composables/useAuth';
import { useFormErrors } from '@/composables/useFormErrors';

import type { RegisterForm } from '@/types/accountForm'

const MIN_PASSWORD_LENGTH = 8;

const router = useRouter();

const form = reactive<RegisterForm>({
  name: '',
  email: '',
  password: '',
  password_confirm: '',
});

const { mutate: register, isPending } = useRegister();
const { errors, formError, clear, setFromApi } = useFormErrors();

function validate(): boolean {
  const found: Record<string, string> = {};

  if (!form.name.trim()) found.name = 'Informe seu nome.';
  if (!form.email.trim()) found.email = 'Informe seu e-mail.';

  if (form.password.length < MIN_PASSWORD_LENGTH) {
    found.password = `A senha deve ter pelo menos ${MIN_PASSWORD_LENGTH} caracteres.`;
  }

  if (form.password !== form.password_confirm) {
    found.password_confirm = 'As senhas não conferem.';
  }

  errors.value = found;
  return Object.keys(found).length === 0;
}

function onSubmit() {
  clear();
  if (!validate()) return;

  register(
    { ...form, name: form.name.trim(), email: form.email.trim() },
    {
      onSuccess: () => router.push({ name: 'login', query: { registered: '1' } }),
      onError: setFromApi,
    },
  );
}
</script>
<template>
  <div class="container flex justify-center my-8 lg:my-16">
    <form
      class="w-full max-w-120 flex flex-col gap-4 p-6 rounded-2xl bg-white shadow-md lg:p-8"
      novalidate
      @submit.prevent="onSubmit"
    >
      <ECInput
        id="name"
        v-model="form.name"
        label="Nome"
        type="text"
        placeholder="John Doe"
        autocomplete="name"
        required
        :error="errors.name"
      />

      <ECInput
        id="email"
        v-model="form.email"
        label="E-mail"
        type="email"
        placeholder="seuemail@exemplo.com"
        autocomplete="email"
        required
        :error="errors.email"
      />

      <ECInput
        id="password"
        v-model="form.password"
        label="Senha"
        type="password"
        placeholder="Digite sua senha"
        autocomplete="new-password"
        required
        :error="errors.password"
      />

      <ECInput
        id="password-confirm"
        v-model="form.password_confirm"
        label="Confirmar senha"
        type="password"
        placeholder="Digite sua senha"
        autocomplete="new-password"
        required
        :error="errors.password_confirm"
      />

      <p v-if="formError" class="text-red-700" role="alert">
        {{ formError }}
      </p>

      <ECButton type="submit" color="secondary" :disabled="isPending">
        {{ isPending ? 'Salvando...' : 'Salvar' }}
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
