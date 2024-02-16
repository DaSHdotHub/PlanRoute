<template>
    <div>
      <HeaderComponent />
      <div class="about-page-container">
        <h2>About Page</h2>
        <!-- Add your content for the About page here -->
      </div>
      <FooterComponent />
    </div>
  </template>
  
  <script>
  import HeaderComponent from '@/components/shared/HeaderComponent.vue';
  import FooterComponent from '@/components/shared/FooterComponent.vue';
  
  export default {
    components: {
      HeaderComponent,
      FooterComponent
    }
  };
  </script>
  
  <style scoped>
  .about-page-container {
    /* Add styling for the about page content container if needed */
  }
  </style>
  