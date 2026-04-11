<script setup>
import { ref } from 'vue'
import { useRoute,useRouter } from 'vue-router'
import Navbar from './Navbar.vue'

const route = useRoute()
const router = useRouter()

const aId = route.params.id
const patId = route.params.patid
const docId = route.params.docid
console.log('pat id',patId,aId,docId)

const name =ref('')
const visit_type = ref('')
const diagnosis = ref('')
const notes = ref('')
const medicines_name = ref('')
const dosage = ref('')
const duration = ref('')



async function getName() {
  const response = await fetch('http://127.0.0.1:5000/api/name', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      patient_id: patId,
      doctor_id: docId
    })
  })

  const result = await response.json()
  name.value = result[0]
  console.log('Name:', name.value.Patient_name)
}

async function Updatepats() {
    const user = {
    doctor_id :docId,
    patient_id : patId,
    appointment_id : aId,
    visit_type : visit_type.value,
    diagnosis : diagnosis.value,
    notes : notes.value,
    medicines_name : medicines_name.value,
    dosage : dosage.value,
    duration : duration.value
}
const response = await fetch('http://127.0.0.1:5000/api/recpat',{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        });
        const result = await response.json()
        router.push('/doctor')
      }


getName()
</script>

<template>
    <Navbar />
  <div class="container mt-4">
    
    <h4>Patient Name: {{ name.Patient_name }}</h4>
    <h2>Update Patient Record</h2>

    <div class="row mb-3">
      <div class="col-md-6">
        <label>Visit Type</label>
        <input v-model="visit_type" class="form-control" placeholder="e.g. Checkup" />
      </div>

      <div class="col-md-6">
        <label>Diagnosis</label>
        <input v-model="diagnosis" class="form-control" placeholder="Diagnosis" />
      </div>
    </div>

    <div class="mb-3">
      <label>Notes</label>
      <textarea v-model="notes" class="form-control"></textarea>
    </div>

    <h5>Prescription</h5>

    <div class="row mb-3">
      <div class="col-md-4">
        <input v-model="medicines_name" class="form-control" placeholder="Medicine Name" />
      </div>

      <div class="col-md-4">
        <input v-model="dosage" class="form-control" placeholder="Dosage" />
      </div>

      <div class="col-md-4">
        <input v-model="duration" class="form-control" placeholder="Duration" />
      </div>
    </div>

    <div class="text-end">
      <button class="btn btn-success" @click="Updatepats">
        Save
      </button>
    </div>

  </div>
</template>
