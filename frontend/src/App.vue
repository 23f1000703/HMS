<script setup>
import { RouterLink, RouterView, useRoute } from 'vue-router'
const route = useRoute()
</script>

<template>
  <div class="container-fluid">
      <nav v-if="route.path == '/login' || route.path == '/patientregister' ||route.path == '/' " class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <RouterLink class="navbar-brand" to="/">Hospital Managment System</RouterLink>

              <div class="ms-auto d-flex gap-2">
              <RouterLink class="nav-btn login-btn" to="/login">Login</RouterLink>
              <RouterLink class="nav-btn register-btn" to="/patientregister">Register</RouterLink>
              </div>
        </div>
      </nav>
    <RouterView />
    </div>

</template>

<style scoped>
/* NAVBAR BASE (SOFT BROWN) */
.navbar {
  background: #8b5e3c !important;   /* main brown */
  padding: 14px 24px;
  border-bottom: 1px solid #7a5134;
}

/* BRAND */
.navbar-brand {
  font-weight: 600;
  font-size: 18px;
  color: #fef3c7 !important;  /* soft cream */
  letter-spacing: 0.3px;
}

/* BUTTON BASE */
.nav-btn {
  text-decoration: none;
  padding: 6px 16px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  transition: 0.25s;
}

/* LOGIN (LIGHT OUTLINE FEEL) */
.login-btn {
  color: #fef3c7;
  border: 1px solid rgba(255,255,255,0.3);
}

.login-btn:hover {
  background: rgba(255,255,255,0.15);
}

/* REGISTER (HIGHLIGHT BUTTON) */
.register-btn {
  background: #facc15;   /* golden highlight */
  color: #3f2a1d;
}

.register-btn:hover {
  background: #eab308;
  transform: translateY(-1px);
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}
</style>