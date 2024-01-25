<!-- News-->
<template>
    <b-container>
        <b-row>
            <b-col>
                <h2>Latest News</h2>
                <b-list-group>
                    <b-list-group-item href="#" active>
                        <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">Version Update</h5>
                            <small>3 days ago</small>
                        </div>
                        <p class="mb-1">Details about the latest version of the website.</p>
                    </b-list-group-item>
                </b-list-group>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
export default {
};
</script>

<style scoped>
/* Styling for the News section */
.news-section {
    padding: 2rem 0;
}

.news-item {
    border-bottom: 1px solid #ddd;
    padding: 1rem 0;
}
</style>
