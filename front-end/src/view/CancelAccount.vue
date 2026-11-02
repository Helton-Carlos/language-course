<script lang="ts" setup>
import { computed, ref } from 'vue';
import { useRouter } from 'vue-router';
import ECBackButton from '@/components/ECBackButton/ECBackButton.vue';
import ECButton from '@/components/ECButton/ECButton.vue';
import ECInput from '@/components/ECInput/ECInput.vue';
import { useDeleteAccount } from '@/composables/useAccount';
import { useFormErrors } from '@/composables/useFormErrors';
import { MESSAGES } from '@/utils/message';

const router = useRouter();

const password = ref('');
const confirmed = ref(false);

const { mutate: deleteAccount, isPending } = useDeleteAccount();
const { errors, clear, setFromApi } = useFormErrors();

const canSubmit = computed(() => confirmed.value && password.value.length > 0 && !isPending.value);

function onSubmit() {
  clear();
  if (!canSubmit.value) return;

  deleteAccount(password.value, {
    onSuccess: () => router.push({ name: 'login' }),
    onError: setFromApi,
  });
}
</script>

<template>
  <section class="max-w-2xl">
    <ECBackButton :to="{ name: 'dashboard' }" />

    <h1 class="mt-4 text-3xl font-bold">
      Cancelar conta
    </h1>

    <p class="mt-2 text-quaternary">
      Sua conta será apagada, junto com seu nome, e-mail, idioma e nível. Essa ação não pode ser desfeita.
    </p>

    <form
      class="mt-6 flex flex-col gap-4 rounded-2xl bg-white p-6 shadow-sm"
      novalidate
      @submit.prevent="onSubmit"
    >
      <label class="flex cursor-pointer items-start gap-3">
        <input
          v-model="confirmed"
          type="checkbox"
          class="mt-1 h-4 w-4 accent-secondary"
        >
        <span>Entendo que a exclusão da conta é permanente.</span>
      </label>

      <ECInput
        id="password"
        v-model="password"
        label="Confirme sua senha"
        type="password"
        placeholder="Digite sua senha"
        autocomplete="current-password"
        required
        :error="errors.password"
      />

      <ECButton type="submit" color="secondary" :disabled="!canSubmit">
        {{ isPending ? MESSAGES.pending.accountDelete : 'Cancelar minha conta' }}
      </ECButton>
    </form>
  </section>
</template>
