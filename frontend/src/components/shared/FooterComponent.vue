<template>
  <b-footer class="text-muted">
    <b-container>
      <p>© 2024 by Your Name</p>
      <p>
        <b-link href="https://linkedin.com" target="_blank">LinkedIn</b-link> |
        <b-link href="https://xing.com" target="_blank">Xing</b-link> |
        <b-link href="https://github.com" target="_blank">GitHub</b-link>
      </p>
    </b-container>
  </b-footer>
</template>
  
<script>
export default {
  // Component logic here
};
</script>

<style scoped>
/* Styling for the Footer */
footer {
  background-color: #98ff98; /* Mint color */
  color: white;
  text-align: center;
  padding: 1rem 0;
}

footer a {
  color: #fff;
  margin: 0 10px;
  transition: color 0.3s ease;
}

footer a:hover {
  color: #ddd;
}
</style>
