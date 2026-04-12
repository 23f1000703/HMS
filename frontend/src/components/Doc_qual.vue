<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Navbar from './Navbar.vue'

const router = useRouter()
const route = useRoute()

const doc_id =route.params.id 
const doctor = ref(null)
const patId =localStorage.getItem("patId")
const userId = localStorage.getItem('user_id')
async function postDoctors() {
    const response = await fetch("http://127.0.0.1:5000/api/doclist",{
    method : 'POST',
     headers:{
         'Content-Type': 'application/json'
          },
          body: JSON.stringify({id : doc_id})
    });
    const data = await response.json()
    console.log('data',data)
    doctor.value = data[0]
    console.log('value',doctor.value)

}

function goBack() {
  router.back()
}

function checkAvailability(doctId,patId) {
    router.push(`/docavail/${doctId}/${patId}`)
}

postDoctors()
</script>

<template>
  <Navbar />
<div class="container mt-5">
    <div class="doctor-card">


      <div class="doctor-info" v-if="doctor">
        <h2 class="name">Dr. {{ doctor.name }}</h2>

        <p class="qualification">The Qualification of {{ doctor.name }} : 
          {{ doctor.qualification }}
        </p>

        <p class="specialization"> Department :  
          {{ doctor.specialization }}
        </p>

        <p class="experience"> Have
          {{ doctor.experience_year }} Years of Experience Overall
        </p>

        <p class="description">
          Dr. {{ doctor.name }} is a {{ doctor.specialization }} in India and has
          an experience of {{ doctor.experience_year }} years in this field.
        </p>
      </div>
    </div>


    <div class="buttons">
      <button class="btn btn-outline-primary" @click="checkAvailability(doctor.id,patId)">
        check availability
      </button>

      <button class="btn btn-outline-secondary" @click="goBack">
        Go Back
      </button>
    </div>
  </div>
</template>


<style scoped>
/* CONTAINER CENTER */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* DOCTOR CARD */
.doctor-card {
  background: #ffffff;
  padding: 30px 35px;
  border-radius: 14px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.08);
  max-width: 750px;
  width: 100%;
  margin-bottom: 20px;
}

/* NAME */
.name {
  font-size: 28px;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 15px;
}

/* INFO TEXT */
.doctor-info p {
  font-size: 15px;
  color: #475569;
  margin-bottom: 10px;
  line-height: 1.6;
}

/* LABEL HIGHLIGHT */
.qualification,
.specialization,
.experience {
  font-weight: 500;
  color: #1e293b;
}

/* DESCRIPTION */
.description {
  margin-top: 10px;
  font-style: italic;
  color: #64748b;
}

/* BUTTON CONTAINER */
.buttons {
  display: flex;
  gap: 15px;
  justify-content: center;
}

/* BUTTON BASE */
.buttons .btn {
  padding: 8px 18px;
  border-radius: 8px;
  font-size: 14px;
  transition: 0.25s;
}

/* COMMON BUTTON STYLE */
.buttons .btn {
  padding: 9px 20px;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.25s ease;
}

/* 🟢 CHECK AVAILABILITY (GREEN THEME) */
.btn-outline-primary {
  border: 2px solid #22c55e;   /* green */
  color: #15803d;
  background: rgba(34, 197, 94, 0.08);
}

.btn-outline-primary:hover {
  background: #22c55e;
  color: white;
  box-shadow: 0 4px 12px rgba(34, 197, 94, 0.4);
  transform: translateY(-2px);
}

/* ⚫ GO BACK (SOFT DARK GREEN-GREY) */
.btn-outline-secondary {
  border: 2px solid #4b5563;
  color: #374151;
  background: rgba(75, 85, 99, 0.05);
}

.btn-outline-secondary:hover {
  background: #4b5563;
  color: white;
  box-shadow: 0 4px 12px rgba(75, 85, 99, 0.4);
  transform: translateY(-2px);
}
</style>