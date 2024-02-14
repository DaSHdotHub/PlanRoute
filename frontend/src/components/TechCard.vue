<template>
  <div class="tech-card-container">
    <div 
      v-for="(tech, index) in technologies" 
      :key="index" 
      class="tech-card" 
      @mouseover="hoveredCard = index" 
      @mouseleave="hoveredCard = null"
      :class="{ 'hover': hoveredCard === index, 'shrink': hoveredCard !== null && hoveredCard !== index }"
    >
      <img :src="tech.imgSrc" alt="Technology Logo" class="tech-logo">
      <p>{{ tech.name }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      technologies: [
        { name: 'TomTom', imgSrc: require('@/assets/images/tomtom_logo.webp') },
        { name: 'Django', imgSrc: require('@/assets/images/django_logo.webp') },
        { name: 'Vue.js', imgSrc: require('@/assets/images/bootstrapvue_logo.webp') },
        { name: 'Python', imgSrc: require('@/assets/images/python-powered_logo.webp') }
      ],
      hoveredCard: null,
    };
  },
};
</script>

<style scoped>
.tech-card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
}

.tech-card {
  flex: 1 1 auto;
  margin: 10px;
  text-align: center;
  transition: transform 0.3s ease;
  border-radius: 100%;
  overflow: hidden; 
}

.tech-card:hover {
  transform: scale(1.5); /* Enlarges the hovered card */
}

.tech-logo {
  width: 80px;
  height: auto;
  transition: width 0.3s ease;
}

.tech-card:hover .tech-logo {
  width: 120px; /* Enlarge logos by 50% */
}

/* Custom positioning to attempt a 'W' shape */
.tech-card:nth-child(1), .tech-card:nth-child(4) {
  margin-top: 50px;
}

.tech-card:nth-child(2), .tech-card:nth-child(3) {
  margin-bottom: 50px;
}
</style>
