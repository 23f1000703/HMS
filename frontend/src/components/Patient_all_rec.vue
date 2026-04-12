<script setup>
import { ref } from 'vue'
import { useRoute,useRouter } from 'vue-router'
import Navbar from './Navbar.vue'

const role =localStorage.getItem('role')
console.log('role',role)
const router = useRouter()
const route = useRoute()
const pat_id = route.params.patid
const doc_id = 1
console.log("these are ids pat all rec",pat_id)



const historyData =ref('')
async function patienthistory(){
  const response = await fetch('http://127.0.0.1:5000/api/patfullrec', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({pat_id: pat_id})
    })

    const result = await response.json()
    historyData.value = result

    console.log('history', historyData.value)
}


patienthistory()

function goBack() {
  router.back()
}


async function exportCSV() {
  console.log("Export CSV clicked")

  const pat_id = Number(localStorage.getItem("patId"))

  const res = await fetch('http://127.0.0.1:5000/api/appointmentsdone')
  const data = await res.json()

  const patientData = data.filter(item => item.patient_id === pat_id)

  if (!patientData.length) {
    alert("No data found")
    return
  }

  const headers = Object.keys(patientData[0]).join(',')
  const rows = patientData.map(row =>
    Object.values(row).map(val => `"${val}"`).join(',')
  )

  const csv = [headers, ...rows].join('\n')

  const blob = new Blob([csv], { type: 'text/csv' })
  const url = window.URL.createObjectURL(blob)

  const a = document.createElement('a')
  a.href = url
  a.download = `patient_${pat_id}.csv`
  a.click()

  window.URL.revokeObjectURL(url)
}
</script>

<template>
  <Navbar />
  <div class="container mt-4 border rounded p-4 bg-white shadow-sm">

    <div class="d-flex justify-content-between align-items-center mb-3 border-bottom pb-2">

      <h2 class="fw-semibold text-dark mb-0">Patient History</h2>
      <button class="btn btn-outline-secondary btn-sm px-3" @click="exportCSV()">Export as CSV</button>

      <button class="btn btn-outline-secondary btn-sm px-3" @click="goBack">
        back
      </button>
    </div>

    <div class="mb-3 fs-6 bg-light p-3 rounded border">
      <div><span class="text-muted">Patient Name:</span> <span class="fw-medium text-uppercase">{{ historyData[0].patient_name }}</span></div>


    <div class="table-responsive border rounded">

      <table class="table table-hover align-middle mb-0">

        <thead class="table-light">
          <tr class="text-secondary small">
            <th>Visit No.</th>
            <th>Department</th>
            <th>Doctor Name</th>
            <th>Visit Type</th>
            <th>Tests Done</th>
            <th>Prescription</th>
            <th>Medicines</th>
            <th>Dosage</th>
            <th>Duration</th>            
          </tr>
        </thead>

        <tbody>
          <tr v-for="item in historyData" :key="item.record_id">
            <td class="fw-medium">{{item.record_id}}</td>
            <td>{{ item.dep }}</td>
            <td>{{ item.doc_name }}</td>
            <td>{{ item.visit_type }}</td>
            <td>{{item.diagnosis}}</td>
            <td class="text-muted">{{ item.notes }}</td>
            <td>{{ item.medicine_name }}</td>
            <td>{{ item.dosage }}</td>
            <td>{{ item.duration }}</td>            
          </tr>
        </tbody>

      </table>

    </div>

  </div>
  </div>
</template>

<style>
.container {
  max-width: 1000px;
}

table th {
  font-weight: 500;
  letter-spacing: 0.3px;
}

table td {
  font-size: 14px;
}

.table-hover tbody tr:hover {
  background-color: #f8f9fa;
}
</style>