<script setup lang="ts">
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}
</script>

<template>
  <footer class="bg-black py-16">
    <div class="container flex justify-between">
      <p class="text-white">
        Explore um novo idioma
        Pequenos passos, grandes conquistas.
      </p>

      <a href="#" @click.prevent="scrollToTop">
        <img src="/logo-white.png" alt="Voltar ao topo">
      </a>

      <p class="text-white">
        Pratique todos os dias.
      </p>
    </div>
  </footer>
</template>
