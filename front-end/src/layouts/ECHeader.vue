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

      <nav v-if="!user">
        <ul class="hidden md:flex md:items-center md:gap-4">
          <li>
            <router-link class="btn btn-primary" to="/documentacao">
              Início
            </router-link>
          </li>
          <li>
            <router-link class="btn btn-primary" to="/idiomas">
              Idioma
            </router-link>
          </li>
          <li>
            <router-link class="btn btn-primary" to="/documentacao">
              Sobre
            </router-link>
          </li>
        </ul>
      </nav>

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
