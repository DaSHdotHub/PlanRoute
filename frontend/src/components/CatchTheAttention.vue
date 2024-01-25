<template>
    <section class="hero-section">
        <b-container>
            <b-row>
                <b-col cols="12" md="8">
                    <h1>Welcome to PlanRoute or VectorGraphic</h1>
                    <p class="lead">Catchy slogan or brief introduction</p>
                    <p> Only X calculations for today left!</p>
                    <b-button variant="primary" size="lg" @click="goToRegister" >Get Started</b-button>
                </b-col>
            </b-row>
        </b-container>
    </section>
</template>

<script>
export default {
    methods: {
        goToRegister() {
            this.$router.push({ name: 'Register' });
        }
    }
};
</script>