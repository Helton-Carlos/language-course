<script lang="ts" setup>
import { computed, reactive } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import ECButton from '@/components/ECButton/ECButton.vue';
import ECInput from '@/components/ECInput/ECInput.vue';
import { useLogin } from '@/composables/useAuth';
import { useFormErrors } from '@/composables/useFormErrors';

import type { LoginForm } from '@/types/accountForm'

const route = useRoute();
const router = useRouter();

const form = reactive<LoginForm>({
  email: '',
  password: '',
});

const { mutate: login, isPending } = useLogin();
const { formError, clear, setFromApi } = useFormErrors();

const justRegistered = computed(() => route.query.registered === '1');

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
      <p v-if="justRegistered" class="rounded-md bg-quinary/15 px-4 py-2 text-tertiary" role="status">
        Conta criada com sucesso. Faça login para continuar.
      </p>

      <ECInput
        id="email"
        v-model="form.email"
        label="E-mail"
        type="email"
        placeholder="seuemail@exemplo.com"
        autocomplete="email"
        required
      />

      <ECInput
        id="password"
        v-model="form.password"
        label="Senha"
        type="password"
        placeholder="Digite sua senha"
        autocomplete="current-password"
        required
      />

      <p v-if="formError" class="text-red-700" role="alert">
        {{ formError }}
      </p>

      <ECButton type="submit" color="secondary" :disabled="isPending || !form.email || !form.password">
        {{ isPending ? 'Entrando...' : 'Entrar' }}
      </ECButton>

      <router-link class="btn btn-border text-center" to="/criar-conta">
        Criar conta
      </router-link>
    </form>
  </div>
</template>
