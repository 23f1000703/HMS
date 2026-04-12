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
      <h2>Welcome,</h2>
      <h3><b>Admin</b></h3>
     <div class="d-flex align-items-right mb-3">

      <button type="button" class="btn btn-success px-4 py-2" style="font-size: 15px; font-weight: 500;" @click ='Create'>Register Doctor</button>
     </div> 
    </div>
  </div>
</template>

<style scoped>
/* REMOVE BOX LOOK */
.container {
  background: transparent;
  box-shadow: none;
  padding: 0;
}

/* WELCOME TEXT */
h2:first-child {
  font-size: 26px;
  font-weight: 400;
  color: #111b22;   /* soft grey */
  margin-bottom: 0;
}

/* NAME (main highlight) */
h2.text-uppercase {
  font-size: 32px;
  font-weight: 700;
  color: #425ea0;   /* strong dark */
  letter-spacing: 1px;
}

/* spacing between welcome and name */
h2 + h2 {
  margin-top: 5px;
}

/* ADMIN TITLE */
h2 {
  font-family: 'Segoe UI', sans-serif;
}

/* SEARCH AREA (clean look, no heavy styling) */
.form-select,
.form-control {
  border-radius: 6px;
  border: 1px solid #cbd5e1;
  font-size: 14px;
}

/* BUTTON CLEAN STYLE */
.btn-primary {
  background: #38bdf8;
  border: none;
  border-radius: 6px;
}

.btn-outline-dark {
  border-radius: 6px;
}
</style>