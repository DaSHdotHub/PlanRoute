<template>
  <footer class="footer">
    <!-- Social Media Icons -->
    <div class="container p-4 pb-0">
      <section class="mb-4">
        <!-- GitHub -->
        <a class="btn text-white btn-floating m-1 icon-hover" style="background-color: #CD5C5C;" href="https://github.com/yourusername" role="button">
          <i class="fab fa-github"></i>
        </a>

        <!-- LinkedIn -->
        <a class="btn text-white btn-floating m-1 icon-hover" style="background-color: #0077b5;" href="https://linkedin.com/in/yourusername" role="button">
          <i class="fab fa-linkedin-in"></i>
        </a>

        <!-- Xing -->
        <a class="btn text-white btn-floating m-1 icon-hover" style="background-color: #FF6347;" href="https://xing.com/profile/yourusername" role="button">
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

<style scoped>
/* Styling for the Footer */
.footer {
  background-color: #FFA07A; /* Lighter Coral */
  position: fixed;
  bottom: 0;
  width: 100%;
}

.btn-floating {
  height: 40px;
  display: inline-block;
  margin-right: 10px;
  border-radius: 50%;
  color: #fff;
  font-size: 20px;
  transition: transform 0.2s ease-in-out; /* Add transition for icon size */
}

.icon-hover:hover {
  transform: scale(1.1); /* Enlarge the icon on hover */
}

.footer-bottom {
  margin: 0;
  color: #fff;
  background-color: #FF6A80; /* Darker Coral Pink */
}
</style>
