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

function Back(){
    router.back()
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
    <button class="btn btn-danger mt-2" @click="Back">Back</button>
  </div>
</template>

<style scoped>
/* MAIN CONTAINER FIX */
.container.mt-4 {
  max-width: 500px;
  margin: 40px auto;     /* ⬅️ center fix */
  background: #ffffff;
  padding: 25px 30px;
  border-radius: 12px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

/* HEADING */
h3 {
  text-align: center;
  font-weight: 600;
  color: #0f172a;
  margin-bottom: 20px;
}

/* LABEL */
label {
  font-size: 14px;
  font-weight: 500;
  color: #374151;
}

/* INPUTS */
.form-control,
.form-select,
textarea {
  border-radius: 8px;
  border: 1px solid #cbd5e1;
  padding: 8px;
  font-size: 14px;
}

/* FOCUS */
.form-control:focus,
.form-select:focus,
textarea:focus {
  border-color: #22c55e;
  box-shadow: 0 0 4px rgba(34, 197, 94, 0.3);
}

/* SPACING */
.mb-2 {
  margin-bottom: 12px;
}

/* BUTTON */
.btn-success {
  width: 100%;
  border-radius: 8px;
  padding: 9px;
  font-size: 14px;
  background: #22c55e;
  border: none;
}

.btn-success:hover {
  background: #16a34a;
}
.btn-danger {
  width: 100%;
  border-radius: 8px;
  padding: 9px;
  font-size: 14px;
  background: #ef4444;
  border: none;
}

.btn-danger:hover {
  background: #dc2626;
}
</style>