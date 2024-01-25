<!-- LandingPage-->
<template>
  <HeaderComponent />
  <TechCard />
  <CatchTheAttention />
  <NewsList />
  <FooterComponent />
</template>

<script>
import HeaderComponent from '@/components/shared/HeaderComponent.vue';
import FooterComponent from '@/components/shared/FooterComponent.vue';
import CatchTheAttention from '@/components/CatchTheAttention.vue';
import TechCard from '@/components/TechCard.vue';
import NewsList from '@/components/NewsList.vue';

export default {
  name: 'LandingPage',
  components: {
    HeaderComponent,
    CatchTheAttention,
    TechCard,
    NewsList,
    FooterComponent
  }
};
</script>

<style>
.hero-section {
  background-image: url('');
  background-size: cover;
  padding: 60px 0;
}
</style>
  