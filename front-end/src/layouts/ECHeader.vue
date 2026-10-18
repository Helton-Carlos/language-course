<script setup lang="ts">
</script>

<template>
  <header class="bg-primary py-8">
    <div class="w-[80%] flex justify-between items-center mx-auto">
      <router-link to="/">
        <img src="/logo.svg">
      </router-link>

      <nav>
        <ul class="hidden md:flex md:items-center md:gap-4">
          <li>
            <router-link class="btn btn-primary" to="/config">
              Início
            </router-link>
          </li>
          <li>
            <router-link class="btn btn-primary" to="/config">
              Idioma
            </router-link>
          </li>
          <li>
            <router-link class="btn btn-primary" to="/config">
              Sobre
            </router-link>
          </li>
        </ul>
      </nav>

      <div class="flex gap-4">
        <router-link class="btn btn-border" to="/config">
          Configuração
        </router-link>

        <router-link class="btn btn-secondary" to="/login">
          Login
        </router-link>
      </div>
    </div>
  </header>
</template>
