<template>
  <footer class="footer text-center">
  <!-- Social Media Icons -->
  <div class="container p-4 pb-0">
    <section class="mb-4">
      <!-- GitHub -->
      <a class="btn text-white btn-floating m-1" style="background-color: #333333;" href="https://github.com/yourusername" role="button">
        <i class="fab fa-github"></i>
      </a>

      <!-- LinkedIn -->
      <a class="btn text-white btn-floating m-1" style="background-color: #0077b5;" href="https://linkedin.com/in/yourusername" role="button">
        <i class="fab fa-linkedin-in"></i>
      </a>

      <!-- Xing -->
      <a class="btn text-white btn-floating m-1" style="background-color: #006567;" href="https://xing.com/profile/yourusername" role="button">
        <i class="fab fa-xing"></i>
      </a>
    </section>
  </div>

  <!-- Copyright -->
  <div class="footer-bottom text-center p-3">
    PlanRoute © 2024 by Daniil Shaulov
  </div>
</footer>
</template>
  
<script>
export default {
  // Component logic here
};
</script>

<style scoped>
/* Styling for the Footer */
.footer {
  background-color: #98ff98; /* Example color */
  position: fixed;
  bottom: 0;
  min-width: 100vw;
}

.btn-floating {
  height: 40px;
  display: inline-block;
  margin-right: 10px;
  border-radius: 50%;
  color: #fff;
  font-size: 20px;
}

.footer-bottom {
  margin: 0;
  color: #fff;
  padding-top: auto;
  margin-top: auto; 
  background-color: #0e6d0e; /* Example color */
}
</style>
