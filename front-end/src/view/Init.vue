<script lang="ts" setup>
import { ref } from 'vue'

const name = ref<string>("init")
</script>

<template>
  <h1>
    {{ name }}
  </h1>
</template>

