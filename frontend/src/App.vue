<script setup>
import { RouterLink, RouterView, useRoute } from 'vue-router'
const route = useRoute()
</script>

<template>
  <div class="container">
      <nav v-if="route.path == '/login' || route.path == '/patientregister' ||route.path == '/' " class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <RouterLink class="navbar-brand" to="/">Hospital Managment System</RouterLink>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <RouterLink class="nav-link" to="/login">Login</RouterLink>
              </li>
            </ul>
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Register
              </button>
              <ul class="dropdown-menu">
                <li><RouterLink class="dropdown-item" to="/patientregister">Register as Patient</RouterLink></li>
                <li><RouterLink class="dropdown-item" to="/doctorregister">Register as Doctor</RouterLink></li>
              </ul>
            </div>
          </div>
        </div>
      </nav>
    <RouterView />
    </div>

</template>

