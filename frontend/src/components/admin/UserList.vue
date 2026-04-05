<script setup>
const { users, title } = defineProps(['users', 'title'])
</script>

<template>
  <div class="container mt-4">

    <!-- Title -->
    <h2 class="mb-3">{{ title }}</h2>

    <!-- List Box -->
    <div class="border p-3 rounded">

      <!-- Each user row -->
      <div 
        v-for="user in users" :key="user.id"
        class="d-flex justify-content-between align-items-center border p-1 mb-1 rounded"
      >
        <!-- Name -->
        <span class="fs-7 text-secondary">
          {{ user.name }}
        </span>

        <!-- Buttons -->
        <div>
          <button class="btn btn-warning me-2">edit</button>
          <button class="btn btn-danger me-2">delete</button>
          <button class="btn btn-secondary">blacklist</button>
        </div>
      </div>

    </div>
  </div>
</template>