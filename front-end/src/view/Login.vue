<script lang="ts" setup>
import { reactive } from 'vue';
import { useRouter } from 'vue-router';
import ECButton from '@/components/ECButton/ECButton.vue';
import ECInput from '@/components/ECInput/ECInput.vue';
import { useLogin } from '@/composables/useAuth';
import { useFormErrors } from '@/composables/useFormErrors';
import { MESSAGES } from '@/utils/message';

import type { LoginForm } from '@/types/accountForm'

const router = useRouter();

const form = reactive<LoginForm>({
  email: '',
  password: '',
});

const { mutate: login, isPending } = useLogin();
const { errors, clear, setFromApi } = useFormErrors();

function onSubmit() {
  clear();

  login(
    { email: form.email.trim(), password: form.password },
    {
      onSuccess: () => router.push({ name: 'dashboard' }),
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
        autocomplete="current-password"
        required
        :error="errors.password"
      />

      <ECButton type="submit" color="secondary" :disabled="isPending || !form.email || !form.password">
        {{ isPending ? MESSAGES.pending.login : 'Entrar' }}
      </ECButton>

      <router-link class="btn btn-border text-center" to="/criar-conta">
        Criar conta
      </router-link>
    </form>
  </div>
</template>
