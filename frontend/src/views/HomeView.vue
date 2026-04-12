<script setup>
</script>

<template>
  <div class="home">

    <div class="hero text-center">
      <h1>Hospital Management System</h1>
      <p>Manage Patients, Doctors and Appointments Easily</p>

      <div class="buttons">
        <router-link to="/login" class="btn btn-primary m-2">Login</router-link>
        <router-link to="/patientregister" class="btn btn-outline-primary m-2">Register</router-link>
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
/* HERO SECTION */
.hero {
  padding: 100px 20px;
  background: linear-gradient(to right, #afbbc2, #dbe5ea);
  border-radius: 0 0 20px 20px;
}

/* HEADING */
.hero h1 {
  font-size: 42px;
  font-weight: 700;
  color: #1e293b;
}

/* SUBTEXT */
.hero p {
  font-size: 18px;
  margin-top: 10px;
  color: #475569;
}

/* BUTTONS */
.buttons {
  margin-top: 25px;
}

.btn {
  padding: 10px 20px;
  border-radius: 8px;
  font-weight: 500;
  transition: 0.3s;
}

/* PRIMARY BUTTON */
.btn-primary {
  background: #38bdf8;
  border: none;
}

.btn-primary:hover {
  background: #0ea5e9;
}

/* OUTLINE BUTTON */
.btn-outline-primary {
  border: 2px solid #38bdf8;
  color: #38bdf8;
}

.btn-outline-primary:hover {
  background: #38bdf8;
  color: white;
}

/* FEATURES SECTION */
.features {
  margin-top: 60px;
}

/* FEATURE CARDS */
.col-md-4 {
  background: #ffffff;
  padding: 25px;
  border-radius: 12px;
  margin-bottom: 20px;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
  transition: 0.3s;
}

/* HOVER EFFECT */
.col-md-4:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}

/* FEATURE TITLES */
.col-md-4 h4 {
  font-weight: 600;
  color: #1e293b;
}

/* FEATURE TEXT */
.col-md-4 p {
  color: #64748b;
  font-size: 14px;
}
</style>