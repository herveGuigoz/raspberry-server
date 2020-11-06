<template>
  <div class="h-screen overflow-hidden">
    <div class="flex flex-no-wrap flex-row justify-between mt-4 px-8">
      <Name/>
      <About
        @open-modal="isOpen = true"
        :isOpen="this.isOpen"
      />
    </div>
    <MainContent/>
    <Contact/>
    <transition
      name="fade"
      @after-enter="showContent = true"
    >
      <modal
        v-if="isOpen"
        @close="isOpen = false"
        @hide-content="showContent = false"
        :showContent="this.showContent"
        :experiences="this.experiences"
        :technos="this.technos"
        :softskills="softskills"
      />
    </transition>
  </div>
</template>

<script>
import Name from '~/components/Name.vue'
import About from '~/components/About.vue'
import Modal from '~/components/Modal'
import Contact from '~/components/Contact'
import MainContent from '~/components/MainContent.vue'

export default {
  name: 'app',
  components: {
    Contact,
    Name,
    About,
    Modal,
    MainContent
  },
  data: function(){
    return {
      isOpen: false,
      showContent: false,
      experiences : [
        {
          titre: 'LEAD DEVELOPPEUR MOBILE - FLUTTER',
          location: 'Bron',
          mission: "Création de l'application NGTV Expérience. State Management avec Riverpod + Hooks + State notifier + Freezed. Networking avec Dio. Tests avec Mockito.",
          techno: ['Dart', 'Flutter', 'Kotlin']
        },
        {
          titre: 'DEVELOPPEUR MOBILE - FLUTTER',
          location: 'Bron',
          mission: "Création d’une application d'arbitrage pour des matchs de foot en salle. State Management avec Riverpod + Hooks + State notifier + Freezed. Networking avec Dio. Tests avec Mockito.",
          techno: ['Dart', 'Flutter', 'Kotlin']
        },
        {
          titre: 'DEVELOPPEUR PHP - SYMFONY',
          location: 'Bron',
          mission: "Développement d’une API Rest (Symfony 4.2.0, API Platform 2.4.5), et d’une solution client en VueJs (utilisation de NuxtJs ^2) pour un projet de capture video de rencontres sportive et mise à dispositions de statistiques individuelles et d’équipes.",
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
        'Dart',
        'Flutter',
        'Kotlin',
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