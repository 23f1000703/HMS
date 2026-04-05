<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

// Dummy data (later API se replace karna)
const doctors = [
  { id: 1, name: "Dr. abcde" },
  { id: 2, name: "Dr. pqrst" },
  { id: 3, name: "Dr. mnop" }
]

// Navigation functions
function goToHistory() {
  router.push('/history')
}

function logout() {
  localStorage.removeItem('token')
  router.push('/login')
}

function checkAvailability(doc) {
  console.log("Checking availability for", doc.name)
}

function viewDetails(doc) {
  router.push(`/doctor/${doc.id}`)
}
</script>

<template>
  <div class="page">


    <div class="header">
      <h1>Department of Oncology</h1>

      <div class="nav-links">
        <span @click="goToHistory">History</span>
        <span @click="logout">Logout</span>
      </div>
    </div>


    <div class="section">
      <h2>Overview</h2>
      <p>
        The Oncology Department in a hospital is dedicated to the diagnosis,
        treatment, and care of patients with cancer. It houses a team of
        specialized doctors, such as medical oncologists, surgical oncologists,
        and radiation oncologists, who work together to provide comprehensive
        cancer care.
      </p>
    </div>


    <div class="section">
      <h2>Doctors' list</h2>

      <div class="doctor-card" v-for="doc in doctors" :key="doc.id">
        <span class="name">{{ doc.name }}</span>

        <div class="actions">
          <button @click="checkAvailability(doc)">
            check availability
          </button>
          <button @click="viewDetails(doc)">
            view details
          </button>
        </div>
      </div>

    </div>

  </div>
</template>

