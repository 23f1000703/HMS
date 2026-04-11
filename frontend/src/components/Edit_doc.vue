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
   </div>
</template>