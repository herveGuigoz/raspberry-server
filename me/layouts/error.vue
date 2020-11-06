<template>
  <div class="h-screen w-screen flex flex-col items-center justify-center">
    <h1 v-if="error.statusCode === 404" class="uppercase">This page doesn’t exist</h1>
    <h1 v-else class="uppercase">An error occurred</h1>
    <NuxtLink to="/" class="text-xs">Home page</NuxtLink>
  </div>
</template>

<script>
  export default {
    layout: 'default',
    props: {
      error: {
        type: Object,
        default: null
      }
    }
  }
</script>
