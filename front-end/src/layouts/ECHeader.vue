<script setup lang="ts">
import { Download, Menu, X } from 'lucide-vue-next';
import { computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useLogout } from '@/composables/useAuth';
import { useCurrentUser } from '@/composables/useCurrentUser';
import { useMobileMenu } from '@/composables/useMobileMenu';
import { usePwaInstall } from '@/composables/usePwaInstall';

const route = useRoute();
const router = useRouter();
const { data: user, isPending } = useCurrentUser();
const { mutate: logout, isPending: isLoggingOut } = useLogout();
const { isOpen, toggle } = useMobileMenu();
const { canInstall, install } = usePwaInstall();

const hasMenu = computed<boolean>(() => !!user.value && route.path.startsWith('/dashboard'));

function signOut() {
  logout(undefined, {
    onSuccess: () => router.push({ name: 'login' }),
  });
}
</script>

<template>
  <header class="bg-primary py-8">
    <div class="container flex items-center justify-between">
      <div class="flex items-center gap-4">
        <button
          v-if="hasMenu"
          type="button"
          class="cursor-pointer rounded-md p-2 text-secondary transition-colors hover:bg-primary-hover lg:hidden"
          :aria-label="isOpen ? 'Fechar menu' : 'Abrir menu'"
          :aria-expanded="isOpen"
          aria-controls="sidebar-nav"
          @click="toggle"
        >
          <X v-if="isOpen" class="h-7 w-7" aria-hidden="true" />
          <Menu v-else class="h-7 w-7" aria-hidden="true" />
        </button>
        <router-link to="/">
          <img src="/logo.svg">
        </router-link>
      </div>
      <div class="flex gap-4">
        <button
          v-if="canInstall"
          type="button"
          class="btn btn-border inline-flex items-center gap-2"
          aria-label="Instalar aplicativo"
          @click="install"
        >
          <Download class="h-5 w-5" aria-hidden="true" />
          <span class="hidden sm:inline">Instalar app</span>
        </button>
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