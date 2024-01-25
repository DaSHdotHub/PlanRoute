<template>
  <div class="tech-stack">
    <b-row>
      <b-col cols="4" v-for="tech in technologies" :key="tech.name">
        <b-card class="tech-card" :title="tech.name" :img-src="tech.img" img-alt="tech.name">
          <p class="card-text">{{ tech.description }}</p>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  props: ['technologies']
};
</script>

<style scoped>
.tech-stack {
  padding: 2rem 0;
}

.tech-card {
  border: none;
  transition: transform 0.3s ease;
  height: calc(100vw / 3 / 1.618); /* Golden ratio */
}

.tech-card:hover {
  transform: scale(1.05);
}
</style>
