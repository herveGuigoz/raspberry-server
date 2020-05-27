<template>
  <div id="name">
    <div class="flex-row">
        <span class="dot" style="transform: matrix(1, 0, 0, 1, 0, 0);"></span>
        <h1 class="firstname">Herve</h1>
      </div>
      <h1 class="lastname">Guigoz</h1>
  </div>
</template>
<script>
export default {
  
}
</script>
<style scoped>
#name {
  padding: 2rem 0;
  display: flex;
  flex-direction: column;
}
.flex-row{
  display: flex;
  flex-direction: row;
  flex-flow: nowrap;
  align-items: center;
}
.dot {
  display: inline-block;
  background-color: #ffffff;
  border-radius: 100%;
  width: 12px;
  height: 12px;
  -webkit-transform: scale(0);
  -ms-transform: scale(0);
  transform: scale(0);
}
.firstname {
    font-size: 16px;
    letter-spacing: 4px;
    margin-left: 0.5rem;
    line-height: 30px;
    font-weight: 400;
    font-style: normal;
    color: #4a5568;
    text-transform: uppercase;
}
.lastname {
  font-size: 20px;
  margin-top: -4px;
  line-height: 18px;
  letter-spacing: 0.12em;
  color: #ffffff;
  text-transform: uppercase;
}
</style>
