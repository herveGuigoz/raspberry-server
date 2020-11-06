<template>
  <button 
      class="outline-none focus:outline-none uppercase font-normal not-italic text-xs"
      @click="$emit('open-modal')"
    >
      {{ isOpen ? "Close" : "About" }}
  </button>
</template>

<script>
export default {
  name: 'About',
  props: {
    isOpen: Boolean
  }
}
</script>

<style scoped>
button {
  color: #ffffff;
  background: transparent;
  letter-spacing: .23px;
  text-align: right;
  text-decoration: none;
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-image: linear-gradient(
		to right,
		#4a5568,
		#4a5568 50%,
		#ffffff 50%);
		background-size: 200% 100%;
		background-position: 101%;
}
button:hover {
  transition: all 0.3s cubic-bezier(0.000, 0.000, 0.230, 1);
  background-position: 0%;
}
</style>