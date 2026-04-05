<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function goBack() {
  router.push('/patient')
}

function exportCSV() {
  console.log("Export CSV clicked")
}
</script>

<template>
  <div class="container mt-4 border rounded p-4">

    <!-- Top Header -->
    <div class="d-flex justify-content-between align-items-center mb-3">

      <h2 class="fw-semibold">Patient History</h2>

      <div class="d-flex gap-2">
        <button class="btn btn-outline-success" @click="exportCSV">
          export as csv
        </button>

        <button class="btn btn-outline-primary" @click="goBack">
          back
        </button>
      </div>

    </div>

    <div class="mb-3 fs-5">
      <div>Patient Name: Mr. abcde</div>
      <div>Doctors' Name: Dr. pqrst</div>
      <div>Department: Cardiology</div>
    </div>


    <div class="table-responsive border rounded">

      <table class="table mb-0">

        <thead class="table-light">
          <tr>
            <th>Visit No.</th>
            <th>Visit Type</th>
            <th>Tests Done</th>
            <th>Diagnosis</th>
            <th>Prescription</th>
            <th>Medicines</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td>1</td>
            <td>In-person</td>
            <td>ECG</td>
            <td>Abnormal Heartbeats</td>
            <td>exercise daily</td>
            <td>Medicine 1</td>
          </tr>

        </tbody>

      </table>

    </div>

  </div>
</template>