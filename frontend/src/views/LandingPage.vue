<!-- LandingPage-->
<template>
    <HeaderComponent />
    <div class="landing-page-container">
    <div class="hero-section" :style="backgroundStyle">
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
  data() {
    return {
      // Dynamically bind the background image style
      backgroundStyle: {
        backgroundImage: `url(${require('@/assets/images/hero_background.webp')})`,
      },
    };
  }
};
</script>

<style>
.landing-page-container {
  min-height: 100vh;
  background: linear-gradient(to right, violet, blue, red); 
  color: #fff; /* Ensures text is readable on the dark background */
}

.hero-section {
  background: image(('@/assets/images/hero_background.webp')); /* Semi-transparent white for contrast */
  margin: 10px 15px 20px; /* Adjust as needed */
  padding: 60px 20px;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
  position: relative; /* Ensures it's above the background gradient */
  z-index: 1; /* Higher than the background but below the header */
}
</style>
