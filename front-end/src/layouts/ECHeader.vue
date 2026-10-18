<script lang="ts" setup>

</script>

<template>
  <header class="bg-primary">
    <div class="flex justify-between text-center items-center mx-8">
      <h1 class="text-2xl font-bold py-4">
        <router-link to="/">
          Languages Course
        </router-link>
      </h1>

      <nav>
        <ul class="hidden md:flex md:items-center md:gap-4">
          <li class="font-medium cursor-pointer hover:underline">Configuração</li>
          <li class="btn btn-secondary">Login</li>
        </ul>
      </nav>
    </div>
  </header>
</template>
