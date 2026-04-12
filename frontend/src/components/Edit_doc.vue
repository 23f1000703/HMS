<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Navbar from './Navbar.vue';

const route = useRoute()
const router = useRouter()



const name = ref ('');
const qualification = ref ('');
const specialization = ref('');
const experience_years = ref ('');

const doctorId = route.params.useId

async function Edit(){
        const doctor = {
        id:doctorId,
        name: name.value,
        specialization: specialization.value,
        qualification: qualification.value,
        experience_years: experience_years.value
    }
    const response = await fetch('http://127.0.0.1:5000/api/docedit',{
        method: 'PUT',
        headers:{
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(doctor)
        });
        console.log(response)
    if(response.ok){
        router.push('/admin')   
    }
}

function Back(){
    router.back()
}
</script>


<template>
  <Navbar />
  <div class="container mt-4" style="max-width: 500px;">

    <h3>Edit Doctor</h3>
    <div class="mb-2">
        <label>Name</label>
        <input v-model="name" class="form-control" required />
    </div>
    <div class="mb-2">
        <label>Specialization</label>
        <select class="form-select" v-model="specialization">
            <option value="">Select Specialization</option>
                            <option>Cardiologist</option>
                            <option>Neurologist</option>
                            <option>Orthopedic</option>
                            <option>Dermatologist</option>
                        </select>
    </div>
    <div class="mb-2">
        <label>Qualification</label>
        <input v-model="qualification" class="form-control" required />
    </div>
    <div class="mb-2">
        <label>Experience</label>
        <input v-model="experience_years" type="number" class="form-control" required />
    </div>
    <button class="btn btn-success mt-2" @click="Edit">Update</button>
    <button class="btn btn-danger mt-2" @click="Back">Back</button>
   </div>
    
</template>

<style scoped>
/* CONTAINER */
.container.mt-4 {
  max-width: 500px;
  margin: 40px auto;
  background: #ffffff;
  padding: 26px 30px;
  border-radius: 14px;
  box-shadow: 0 8px 22px rgba(0,0,0,0.08);
}

/* HEADING */
h3 {
  text-align: center;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 20px;
}

/* LABEL */
label {
  font-size: 14px;
  font-weight: 500;
  color: #374151;
}

/* INPUT */
.form-control,
.form-select {
  border-radius: 8px;
  border: 1px solid #cbd5e1;
  padding: 9px;
  font-size: 14px;
}

/* FOCUS */
.form-control:focus,
.form-select:focus {
  border-color: #22c55e;
  box-shadow: 0 0 5px rgba(34, 197, 94, 0.3);
}

/* BUTTON BASE */
.btn {
  width: 100%;
  border-radius: 10px;
  padding: 10px;
  font-size: 14px;
  margin-top: 10px;
}

/* UPDATE */
.btn-success {
  background: #22c55e;
  border: none;
}

.btn-success:hover {
  background: #16a34a;
}

/* BACK */
.btn-danger {
  background: #ef4444;
  border: none;
}

.btn-danger:hover {
  background: #dc2626;
}
</style>