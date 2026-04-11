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
.doctor-card {
  display: flex;
  justify-content: space-between;
  border: 1px solid #ccc;
  padding: 30px;
  border-radius: 10px;
}

.doctor-info {
  max-width: 70%;
}

.name {
  font-size: 28px;
  font-weight: bold;
}

.qualification,
.specialization,
.experience {
  font-size: 18px;
  margin: 5px 0;
}

.description {
  margin-top: 15px;
  font-size: 16px;
}

.buttons {
  margin-top: 20px;
  display: flex;
  gap: 15px;
}
</style>