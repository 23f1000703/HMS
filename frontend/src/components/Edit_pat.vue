<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Navbar from './Navbar.vue'

const route = useRoute()
const router = useRouter()

const name = ref('')
const dob = ref('')
const phone_no = ref('')
const gender = ref('')
const blood_group = ref('')
const address = ref('')

const patientId = route.params.id   
console.log('edit',patientId)

async function Edit(){
    const patient = {
        id: patientId,
        name: name.value,
        dob: dob.value,
        phone_no: phone_no.value,
        gender: gender.value,
        blood_group: blood_group.value,
        address: address.value
    }

    const response = await fetch('http://127.0.0.1:5000/api/patientedit',{
        method: 'PUT',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(patient)
    })

    console.log(response)

    if(response.ok){
        router.back()   
    }
}
</script>

<template>
  <Navbar />
  <div class="container mt-4" style="max-width: 500px;">

    <h3>Edit Patient</h3>

    <div class="mb-2">
        <label>Name</label>
        <input v-model="name" class="form-control" required />
    </div>

    <div class="mb-2">
        <label>DOB</label>
        <input v-model="dob" type="date" class="form-control" required />
    </div>

    <div class="mb-2">
        <label>Phone</label>
        <input v-model="phone_no" class="form-control" required />
    </div>

    <div class="mb-2">
        <label>Gender</label>
        <select v-model="gender" class="form-select">
            <option value="">Select Gender</option>
            <option>Male</option>
            <option>Female</option>
            <option>Other</option>
        </select>
    </div>

    <div class="mb-2">
        <label>Blood Group</label>
        <select class="form-select" v-model="blood_group">
            <option value="">Select Blood Group</option>
            <option>A+</option>
            <option>A-</option>
            <option>B+</option>
            <option>B-</option>
            <option>O+</option>
            <option>O-</option>
            <option>AB+</option>
            <option>AB-</option>
            </select>
    </div>

    <div class="mb-2">
        <label>Address</label>
        <textarea v-model="address" class="form-control"></textarea>
    </div>

    <button class="btn btn-success mt-2" @click="Edit">Update</button>
  </div>
</template>