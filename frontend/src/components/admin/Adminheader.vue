<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
function Create(){
   router.push('/doctorregister')
}
const role = localStorage.getItem('role')
</script>
<template>
  <div class="container mt-3">

    <div v-if=" role !== 'admin'">
    <h2>Welcome User</h2>
    </div>
    
    <div v-if = "role === 'admin' ">
      <h2>Welcome Admin</h2>
     <div class="d-flex justify-content-between align-items-center mb-3">
      
      <div class="d-flex gap-2">
        <input 
          class="form-control" 
          placeholder="doctor, patient, department..." 
          style="width: 300px;" 
        />
        <button class="btn btn-primary">Search</button>
      </div>

      <button type="button" class="btn btn-outline-dark" @click ='Create'>Create</button>
     </div> 
    </div>
  </div>
</template>