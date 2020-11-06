<template>
  <div class="flex flex-col">
    <div class="flex flex-row items-center">
        <span 
					class="dot inline-block bg-white rounded-full"
					style="transform: matrix(1, 0, 0, 1, 0, 0);"
        />
        <h1 class="firstname">Herve</h1>
      </div>
      <h1 class="lastname">Guigoz</h1>
  </div>
</template>

<script>
export default {
  name: 'Name'
}
</script>

<style scoped>
.dot {
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