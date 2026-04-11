<script setup>
import { ref,watch } from 'vue'
import { useRouter } from 'vue-router'


const router = useRouter()
const props = defineProps({docname: String,patname: String})
function Create(){
   router.push('/doctorregister')
}
const role = localStorage.getItem('role')
</script>
<template>
  <div class="container mt-3">

    <div v-if=" role == 'patient'">
    <h2>Welcome,</h2>
          <h2 class =text-uppercase> {{ patname }}</h2>
    </div>
        <div v-if=" role == 'doctor'">
    <h2>Welcome,</h2>
          <h2 class =text-uppercase>Dr. {{ docname }}</h2>
    </div>
    
    <div v-if = "role === 'admin' ">
      <h2>Welcome Admin</h2>
     <div class="d-flex justify-content-between align-items-center mb-3">
      
      <div class="d-flex gap-2">

        <select v-model="searchType" class="form-select" style="width: 180px;">
          <option disabled value="">Select Search Type</option>
          <option value="patient">Patient Name</option>
          <option value="doctor">Doctor Name</option>
          <option value="department">Department</option>
        </select>

        <input 
          v-model="searchQuery"
          class="form-control" 
          placeholder="Search..." 
          style="width: 250px;" 
        />

        <button class="btn btn-primary" @click="handleSearch">
          Search
        </button>

      </div>

      <button type="button" class="btn btn-outline-dark" @click ='Create'>Create</button>
     </div> 
    </div>
  </div>
</template>