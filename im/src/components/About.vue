<template>
  <div id="about">

    <button @click="$emit('openModal')">
      {{ isOpen ? "Close" : "About" }}
    </button>
  
  </div>
</template>

<script>
export default {
  name: 'About',
  props: {
    isOpen: Boolean
  }
}
</script>

<style lang="scss" scoped>
$main-color: #4a5568;
$secondary-color: #ffffff;

button {
  font-family: Poppins,Helvetica,Arial,sans-serif;
  text-transform: uppercase;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  color: $secondary-color;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  cursor: pointer;
  background: transparent;
  letter-spacing: .23px;
  text-align: right;
  text-decoration: none;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-image: linear-gradient(
        to right,
        $main-color,
        $main-color 50%,
        $secondary-color 50%);
        background-size: 200% 100%;
        background-position: 101%;
}

button:hover {
  transition: all 0.3s cubic-bezier(0.000, 0.000, 0.230, 1);
  background-position: 0%;
}
</style>


