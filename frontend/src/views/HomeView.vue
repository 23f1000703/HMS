<script setup>
</script>

<template>
  <div class="home">

    <!-- Hero Section -->
    <div class="hero text-center">
      <h1>Hospital Management System</h1>
      <p>Manage Patients, Doctors and Appointments Easily</p>

      <div class="buttons">
        <router-link to="/login" class="btn btn-primary m-2">Login</router-link>
        <router-link to="/register" class="btn btn-outline-primary m-2">Register</router-link>
      </div>
    </div>

    <!-- Features Section -->
    <div class="features container mt-5">
      <div class="row text-center">

        <div class="col-md-4">
          <h4>👨‍⚕️ Doctors</h4>
          <p>Manage doctor profiles and availability</p>
        </div>

        <div class="col-md-4">
          <h4>🧑 Patients</h4>
          <p>Track patient records and history</p>
        </div>

        <div class="col-md-4">
          <h4>📅 Appointments</h4>
          <p>Book and manage appointments easily</p>
        </div>

      </div>
    </div>

  </div>
</template>

<style scoped>
.hero {
  padding: 80px 20px;
  background: #f5f7fa;
}

.hero h1 {
  font-size: 40px;
  font-weight: bold;
}

.hero p {
  font-size: 18px;
  margin-top: 10px;
}

.buttons {
  margin-top: 20px;
}
</style>