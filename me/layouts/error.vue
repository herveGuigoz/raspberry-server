<template>
  <div>
    <h1 v-if="error.statusCode === 404">This page doesn’t exist</h1>
    <h1 v-else>An error occurred</h1>
    <NuxtLink to="/">Home page</NuxtLink>
  </div>
</template>

<script>
  export default {
    props: {
      error: {
        type: Object,
        default: null
      }
    }
  }
</script>

<style scoped>
.container {
  font-family: sans-serif;
  padding-top: 10%;
  text-align: center;
}
h1 {
  font-size: 20px;
}
</style>