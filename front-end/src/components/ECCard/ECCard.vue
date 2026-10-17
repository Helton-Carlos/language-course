<script setup lang="ts">
defineSlots<{
  header?(): unknown;
  body?(): unknown;
  footer?(): unknown;
}>();
</script>

<template>
  <article class="flex flex-col overflow-hidden rounded-lg border border-tertiary/15 bg-white shadow-sm">
    <header v-if="$slots.header" class="border-b border-tertiary/15 px-4 py-3 font-semibold text-tertiary">
      <slot name="header" />
    </header>

    <div v-if="$slots.body" class="flex-1 px-4 py-4 text-quaternary">
      <slot name="body" />
    </div>

    <footer v-if="$slots.footer" class="border-t border-tertiary/15 px-4 py-3">
      <slot name="footer" />
    </footer>
  </article>
</template>
