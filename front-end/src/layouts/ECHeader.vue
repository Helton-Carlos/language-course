<script setup lang="ts">
</script>

<template>
  <header class="bg-primary py-8">
    <div class="container flex justify-between">
      <router-link to="/">
        <img src="/logo.svg">
      </router-link>

      <nav>
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
        <router-link class="btn btn-border" to="/documentacao">
          Documentação
        </router-link>

        <router-link class="btn btn-secondary" to="/login">
          Login
        </router-link>
      </div>
    </div>
  </header>
</template>
