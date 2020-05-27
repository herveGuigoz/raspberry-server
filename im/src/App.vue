<template>
  <div id="app">
    <Name/>
    <MainContent/>
    <About
      @openModal="isOpen = true"
      :isOpen="this.isOpen"
    />
    <contact/>
    <transition
      name="fade"
      @after-enter="showContent = true"
    >
      <modal
        v-if="isOpen"
        @close="isOpen = false"
        @hideContent="showContent = false"
        :showContent="this.showContent"
        :experiences="this.experiences"
        :technos="this.technos"
        :softskills="softskills"
      />
    </transition>
  </div>
</template>

<script>
import Name from './components/Name.vue'
import MainContent from './components/MainContent.vue'
import About from './components/About.vue'
import Modal from './components/Modal'
import Contact from "./components/Contact";

export default {
  name: 'app',
  components: {
    Contact,
    Name,
    MainContent,
    About,
    Modal,
  },
  data: function(){
    return {
      isOpen: false,
      showContent: false,
      experiences : [
        {
          titre: 'DEVELOPPEUR PHP - SYMFONY',
          location: 'Bron',
          mission: "Developpement d’une API Rest (Symfony 4.2.0, API Platform 2.4.5), et d’une solution client en VueJs (utilisation de NuxtJs ^2) pour un projet de capture video de rencontres sportive et mise à dispositions de statistiques individuelles et d’équipes.",
          techno: ['Symfony', 'Api plateform', 'VueJS', 'NuxtJs', 'Git', 'PHP Unit']
        },
        {
          titre: 'DEVELOPPEUR PHP - SYMFONY',
          location: 'Lyon',
          mission: "Creation d’un journal vidéo sous Symfony 4. Les fonctionnalités développées sont : la gestion des comptes (créateur et internaute), la gestion des vidéos par le créateur, l’affichage du journal vidéo, la gestion des commentaires, la mise en place de statistiques (vues, likes), la gestion des abonnements et des notifications.",
          techno: ['Symfony', 'Javascript', 'UIkit', 'Git', 'PHP Unit']
        },
        {
          titre: 'DEVELOPPEUR PHP',
          location: 'Lyon',
          mission: 'Creation un site de promotion et de gestion des reservations hôtelière (design pattern MVC) avec manipulation des ressources d’une base de données (MySQL).',
          techno: ['PHP', 'SQL', 'VueJs', 'Javascript', 'Material Design', 'Git']
        }
      ],
      technos : [
        'PHP',
        'Symfony',
        'API Platform',
        'Javascript',
        'Vue.js',
        'NuxtJs',
        'SQL',
        'HTML & CSS & Twig',
        'Git',
        'Methodes Agile / Scrum.',
        'ORM Doctrine',
        'Linux'
      ],
      softskills : [
        'Disponibilité et engagement',
        'Résistance au stress',
        'Initiative',
        'Rigueur et Précision',
        'Respect des règles, des standards et des méthodes',
        'Travail en équipe',
        "Communication aisée, Capacité d'écoute"
      ]
    }
  }
}
</script>

<style>
@import url('./assets/fonts/fonts.css');
html, body {
      background: linear-gradient(315deg, rgba(255,255,255,0.5) 0%, rgba(255,255,255,0) 100%), linear-gradient(315deg, #3eba9b 0%, #16c79e 100%);
}
* {
    vertical-align: baseline;
    border: 0;
    outline: 0;
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
#app {
  padding: 0 2rem;
  height: 100vh;
  display: flex;
  flex-direction: row;
  flex-flow: nowrap;
}

a, abbr, acronym, address, applet, big, blockquote, body, button, caption, cite, code, dd, del, dfn, div, dl, dt, em, fieldset, font, form, h1, h2, h3, h4, h5, h6, html, iframe, img, ins, kbd, label, legend, li, object, ol, p, pre, q, s, samp, small, span, strike, strong, sub, sup, table, tbody, td, tfoot, th, thead, tr, tt, ul, var {
    font-family: Poppins,Helvetica,Arial,sans-serif;
    color: #2b2d30;
    font-family: 'Poppins', sans-serif;
    font-size: 1.4rem;
    line-height: 1.8;
    letter-spacing: .01em;
    font-weight: 400;
    font-style: normal;
    vertical-align: baseline;
    border: 0;
    outline: 0;
    padding: 0;
    margin: 0;
}

.main-content {
  font-size: 2.5rem;
}

.contact {
  width: 100%;
  background: #42b983;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
.fade-enter-active, .fade-leave-active {
  transition: 0.2s opacity ease-out;
}
</style>
