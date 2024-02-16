<template>
  <HeaderComponent />
  <div class="landing-page-container">
    <div class="hero-section">
      <div class="container text-center">
        <h1 class="display-3 text-white">Making Healthcare Navigation Effortless</h1>
        <p class="lead text-white">Discover the easiest way to manage patients' logistics with real-time routing.</p>
        <b-button variant="primary" @click="goToRegister" class="mt-3">Sign Up Now</b-button>
        <b-button variant="success" @click="goToAboutPage" class="mt-3 ml-2">Learn More</b-button>
      </div>
    </div>
    <TechCard />
    <NewsList />
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from '@/components/shared/HeaderComponent.vue';
import FooterComponent from '@/components/shared/FooterComponent.vue';
import TechCard from '@/components/TechCard.vue';
import NewsList from '@/components/NewsList.vue';

export default {
  name: 'LandingPage',
  components: {
    HeaderComponent,
    TechCard,
    NewsList,
    FooterComponent
  },
  methods: {
    goToRegister() {
      this.$router.push({ name: 'Register' });
    },
    goToAboutPage() {
      this.$router.push({ name: 'About' });
    },
  },
};
</script>

<style>
.landing-page-container {
  min-height: 100vh;
}

.hero-section {
  background-image: url('@/assets/images/hero_background.webp');
  background-size: cover; /* Ensure the image covers the entire hero section */
  background-position: center; /* Center the background image */
  padding: 60px 20px;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  position: relative;
  z-index: 1;
}
</style>
