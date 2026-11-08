<script setup lang="ts">
import { useRouter } from 'vue-router';
import { useLogout } from '@/composables/useAuth';
import { useCurrentUser } from '@/composables/useCurrentUser';

const router = useRouter();
const { data: user, isPending } = useCurrentUser();
const { mutate: logout, isPending: isLoggingOut } = useLogout();

function signOut() {
  logout(undefined, {
    onSuccess: () => router.push({ name: 'login' }),
  });
}
</script>

<template>
  <header class="bg-primary py-8">
    <div class="container flex justify-between">
      <router-link to="/">
        <img src="/logo.svg">
      </router-link>

      <div class="flex gap-4">
        <router-link v-if="!user" class="btn btn-border" to="/documentacao">
          Documentação
        </router-link>

        <template v-if="user">
          <router-link class="btn btn-secondary" to="/dashboard">
            Dashboard
          </router-link>

          <button
            type="button"
            class="btn btn-border"
            :disabled="isLoggingOut"
            @click="signOut"
          >
            Sair
          </button>
        </template>

        <router-link v-else-if="!isPending" class="btn btn-secondary" to="/login">
          Login
        </router-link>
      </div>
    </div>
  </header>
</template>
