<template>
  <div
    class="modal"
    @click="$emit('hide-content')"
  >
    <transition
      name="content"
      @after-leave="$emit('close')"
    >
      <div
        v-if="showContent"
        class="content w-11/12 p-8"
        @click.stop
      >
        <h1>Disponible pour de courtes missions freelance.</h1>

        <p>
          Impliqué et curieux, j'aime découvrir de nouvelles technologies.
        </p>

        <div class="flex flex-row pt-8">

          <div class="flex flex-col w-3/5">

            <div class="title text-xxs">experiences</div>
            <div class="bordered"></div>
            <div class="mt-4" v-for="experience in experiences" :key="experience">
              <div class="experiences text-custom-gray text-xxs">
                {{ experience.titre }}
              </div>
              <div class="experiences text-xxs">
                {{ experience.mission }}
              </div>
            </div>
          </div>

          <div class="flex-col ml-8">
            <div class="title text-xxs">Techno</div>
            <div class="bordered"></div>
            <div class="mt-4">
              <div class="experiences text-custom-gray text-xxs" v-for="techno in technos" :key="techno">
                {{ techno }}
              </div>
              <div class="experiences"></div>
            </div>
          </div>
          <div class="flex-col ml-8">
            <div class="title text-xxs">Soft Skill</div>
            <div class="bordered"></div>
            <div class="mt-4">
              <div class="experiences text-custom-gray text-xxs" v-for="softskill in softskills" :key="softskill">
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
  height: 86%;
  overflow: scroll;
  border-radius: 3px;
  color: #c4c3c3;
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
  font-family: 'Poppins-light', 'Helvetica', 'Arial', sans-serif;
  color: #c4c3c3;
  font-style: normal;
  font-weight: 300;
  font-size: 21px;
}
.title {
    font-family: 'Poppins-light', 'Helvetica', 'Arial', sans-serif;
    font-style: normal;
    font-weight: 200;
    color: #000;
    letter-spacing: -.05px;
    text-transform: uppercase;
    position: relative;
}
.text-xxs {
  font-size: 0.5rem;
}

.bordered {
  border-top: 1px solid #c4c3c3!important;
}
.experiences, .competences {
  font-weight: 400;
  font-style: normal;
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
.text-custom-gray {
  color: #c4c3c3;
}
</style>