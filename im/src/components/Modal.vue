<template>
  <div
    class="modal"
    @click="$emit('hideContent')"
  >
    <transition
      name="content"
      @after-leave="$emit('close')"
    >
      <div
        v-if="showContent"
        class="content"
        @click.stop
      >
        <h1>A l'écoute pour un poste de développeur PHP.</h1>

        <p>
          Impliqué et curieux, j'aime découvrir de nouvelles technologies et j'ai le goût du travail bien fait !
        </p>

        <div class="flex-row">

          <div class="flex-col-experiences">

            <div class="title">experiences</div>
            <div class="bordered"></div>
            <div class="col" v-for="experience in experiences" :key="experience">
              <div class="experiences titre pt1">
                {{ experience.titre }}
              </div>
              <div class="experiences">
                {{ experience.mission }}
              </div>
            </div>
          </div>

          <div class="flex-col ml-5">
            <div class="title">Techno</div>
            <div class="bordered"></div>
            <div class="col">
              <div class="experiences titre pt1" v-for="techno in technos" :key="techno">
                {{ techno }}
              </div>
              <div class="experiences"></div>
            </div>
          </div>
          <div class="flex-col ml-5">
            <div class="title">Soft Skill</div>
            <div class="bordered"></div>
            <div class="col">
              <div class="experiences titre pt1" v-for="softskill in softskills" :key="softskill">
                {{ softskill }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name:'modal',
  props: {
    showContent: Boolean,
    experiences : Array,
    competences : String,
    technos: Array,
    softskills: Array
  }
}
</script>

<style scoped>

.modal {
  position: absolute;
  overflow: hidden;
  top: 0;
  left: 0;
  right: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0,0,0,0.6)
}
.content {
  position: absolute;
  bottom: 0;
  right: 0;
  z-index: 99;
  background: #fbfaf7;
  width: 89.5%;
  height: 86%;
  overflow: scroll;
  border-radius: 3px;
  color: #c4c3c3;
  padding: 2rem;
  -webkit-overflow-scrolling: touch;
}
.content > h1 {
  font-style: normal;
  font-weight: 300;
  font-size: 21px;
  line-height: 26px;
  letter-spacing: -.22px;
}
.content > p {
  font-family: Poppins-light,Helvetica,Arial,sans-serif;
  color: #c4c3c3;
  font-style: normal;
  font-weight: 300;
  font-size: 21px;
}
.title {
    font-family: Poppins-light,Helvetica,Arial,sans-serif;
    font-weight: 400;
    font-style: normal;
    font-weight: 200;
    font-size: 0.5rem;
    color: #000;
    letter-spacing: -.05px;
    text-transform: uppercase;
    position: relative;
}

.flex-row {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  justify-content: flex-start;

  padding-top: 2rem;
}
.flex-col-experiences {
  display: flex;
  flex-direction: column;
  width: 40%;
}

.bordered {
  border-top: 1px solid #c4c3c3!important;
  font-size: 0.8rem;
}
.col {
  font-size: 0.8rem;
}
.experiences, .competences {
  font-weight: 400;
  font-style: normal;
  font-size: 14px;
  color: #000;
  letter-spacing: -.17px;
}

.content-enter {
  transform: translateY(100%);
}

.content-leave-to {
  transform: translateY(100%);
}
.content-enter-active, .content-leave-active {
  transition: .4s;
}

.pt1 {padding-top: 0.5rem}

.titre {
  color: #c4c3c3;
}
.ml-5 {
  margin-left:5rem;
}
</style>