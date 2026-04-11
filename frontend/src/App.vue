<script setup>
import { RouterLink, RouterView, useRoute } from 'vue-router'
const route = useRoute()
</script>

<template>
  <div class="container-fluid">
      <nav v-if="route.path == '/login' || route.path == '/patientregister' ||route.path == '/' " class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <RouterLink class="navbar-brand" to="/">Hospital Managment System</RouterLink>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <button><RouterLink class="nav-link" to="/login">Login</RouterLink></button>
              </li>
            </ul>
                        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <button><RouterLink class="nav-link" to="/patientregister">Register</RouterLink></button>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    <RouterView />
    </div>

</template>

<style scoped>
/* NAVBAR DARK (matching soft bg) */
.navbar {
  background: #9e7b07 !important;   /* darker shade of your bg */
  border-bottom: 1px solid #fbfbfb;
  padding: 12px 20px;
}

/* Logo */
.navbar-brand {
  color: #c3ccd4 !important;
  font-weight: bold;
}

/* Links */
.navbar .nav-link {
  color: #e2e8f0 !important;
  transition: 0.3s;
}

/* Hover */
.navbar .nav-link:hover {
  color: #ffffff !important;
}

/* Active route */
.navbar .router-link-active {
  color: #d7dfe2 !important;
  font-weight: 500;
}

/* Mobile icon */
.navbar-toggler-icon {
  filter: invert(1);
}
</style>