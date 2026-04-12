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

function Back(){
  router.back()
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

    <div>
      <button class="btn btn-success" @click="Updatepats">
        Save
      </button>
    </div>
    <div class="text-end">
      <button class="btn btn-danger" @click="Back">
        Back
      </button>
    </div>

  </div>
</template>

<style scoped>
/* MAIN CONTAINER */
.container.mt-4 {
  max-width: 750px;
  margin: 40px auto;
  background: #ffffff;
  padding: 28px 32px;
  border-radius: 14px;
  box-shadow: 0 8px 22px rgba(0,0,0,0.08);
}

/* PATIENT NAME */
h4 {
  font-size: 16px;
  font-weight: 500;
  color: #475569;
  margin-bottom: 5px;
}

/* MAIN TITLE */
h2 {
  font-size: 24px;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 20px;
}

/* SECTION TITLE */
h5 {
  font-size: 18px;
  font-weight: 600;
  color: #1e293b;
  margin-top: 15px;
  margin-bottom: 10px;
}

/* LABEL */
label {
  font-size: 13px;
  font-weight: 500;
  color: #374151;
  margin-bottom: 4px;
}

/* INPUTS */
.form-control,
textarea {
  border-radius: 8px;
  border: 1px solid #cbd5e1;
  padding: 9px;
  font-size: 14px;
  transition: 0.2s;
}

/* FOCUS */
.form-control:focus,
textarea:focus {
  border-color: #22c55e;
  box-shadow: 0 0 5px rgba(34, 197, 94, 0.3);
}

/* ROW SPACING */
.row {
  margin-bottom: 12px;
}

/* SAVE BUTTON */
.btn-success {
  border-radius: 10px;
  padding: 8px 22px;
  font-size: 14px;
  font-weight: 500;
  background: #22c55e;
  border: none;
  transition: 0.25s;
}

.btn-success:hover {
  background: #16a34a;
  box-shadow: 0 4px 12px rgba(34, 197, 94, 0.4);
  transform: translateY(-1px);
}
</style>
