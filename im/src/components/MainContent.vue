<template>
  <div id="main-content">
    <div class="me">
      <p ref="anime" id="anime"></p>
    </div>
  </div>
</template>

<script>
import Typed from 'typed.js';
export default {
  name: 'MainContent',
  mounted() {
    let options = {
      strings: ["Les formations que j'ai suivies","Mes différents stages","Mon expérience professionnelle et tous les travaux et projets auxquels j'ai participés m'ont permis d'acquérir de nombreuses compétences dans le domaine du developpement web."],
      //strings: ["<i>First</i> sentence.", "&amp; a second sentence."],
      typeSpeed: 40,
      showCursor: false
    }
    new Typed(this.$refs.anime, options);
  }
}
</script>

<style scoped>
#main-content {
  width: 100vw;
  padding-left: 0;
  margin-left: 0;
}
.me {
  width: 100%;
  height: 90%;
  display: flex;
  align-items: center;
}
p, span {
  font-size: 2.5vw;
  line-height: 4.21875vw;
  letter-spacing: -.4px;
  margin-top: 0;
  color: #4a5568;
  font-family: 'Poppins', sans-serif;
  line-height: 1.8;
  letter-spacing: .01em;
}

/* @media (max-width: 640px) { p,span {font-size:16px; line-height:30px;} } */

.white {
  color:#ffffff;
}

</style>
