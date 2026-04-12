<script setup>
import { ref } from 'vue'
import { useRoute,useRouter } from 'vue-router'
import Navbar from './Navbar.vue'

const Route = useRoute() 
const Router =useRouter()
const schedule = ref([])

const docid = Route.params.docid
const patid = Route.params.patid
const role =localStorage.getItem("role")

const today = new Date()

for (let i = 0; i < 7; i++) {
  const d = new Date()
  d.setDate(today.getDate() + i)
  if (d.getDay() === 0) continue

  schedule.value.push({
    date: d.toISOString().split('T')[0],
    shift: ['Morning', 'Evening']
  })
}

async function bookSlot(date, shift) {

    const response = await fetch('http://127.0.0.1:5000/api/bookslot', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        doc_id: docid,
        pat_id: patid,
        date: date,
        shift: shift
      })
    })
    Router.push('/patient')
}

async function sendSchedule() {
    const response = await fetch('http://127.0.0.1:5000/api/appointment', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({schedule:schedule.value,doc_id:docid})
    })

    const data = await response.json()
    schedule.value= data
    console.log('Response:', schedule.value)
}
function Back(){
  Router.back()
}
sendSchedule()
console.log(schedule.value)
</script>

<template>
<Navbar />
<h3>Doctor's Availability</h3>
<div v-if="role === 'doctor'">
<div v-for="(day,index) in schedule" :key="day.date" class="row mb-2">
  
  <div class="col-3">
    {{ day.date }}
  </div>

  <div class="col-4">
    <span :class="day.shift[0] === 'Avail'
        ? 'text-danger border border-danger p-2' 
        : 'text-success border border-success p-2'">08:00 - 12:00 am</span>
  </div>

  <div class="col-4">
    <span :class="day.shift[1] === 'Avail' 
        ? 'text-danger border border-danger p-2' 
        : 'text-success border border-success p-2'">04:00 - 09:00 pm</span>
  </div>

</div>
</div>
<div v-if="role === 'patient'"> 
  <div v-for="(day,index) in schedule" :key="day.date" class="row mb-2">
    
    <div class="col-3">
      {{ day.date }}
    </div>

    <div class="col-4">
      <span :class="day.shift[0] === 'Avail'
          ? 'text-danger border border-danger p-2' 
          : 'text-success border border-success p-2'">
        08:00 - 12:00 am
      </span>

      <button 
        v-if="day.shift[0] !== 'Avail'" 
        class="btn btn-primary btn-sm mt-1"
        @click="bookSlot(day.date, 'Morning')">
        Book
      </button>
    </div>

    <div class="col-4">
      <span :class="day.shift[1] === 'Avail' 
          ? 'text-danger border border-danger p-2' 
          : 'text-success border border-success p-2'">
        04:00 - 09:00 pm
      </span>

      <button 
        v-if="day.shift[1] !== 'Avail'" 
        class="btn btn-primary btn-sm mt-1"
        @click="bookSlot(day.date, 'Evening')">
        Book
      </button>
    </div>

  </div>
</div>
  <div class="col-1">
    <button class="btn btn-danger btn-sm" @click="Back">
      Back
    </button>
  </div>
</template>

<style scoped>
/* HEADING */
h3 {
  text-align: center;
  font-weight: 700;
  font-size: 24px;
  color: #0f172a;
  margin: 20px 0;
}

/* ROW CARD */
.row {
  background: #ffffff;
  border-radius: 10px;
  padding: 12px 10px;
  margin: 10px auto;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  max-width: 900px;
}

/* DATE COLUMN */
.col-3 {
  font-weight: 600;
  color: #1e293b;
  display: flex;
  align-items: center;
}

/* SHIFT BOX */
.col-4 span {
  display: inline-block;
  width: 100%;
  text-align: center;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 500;
}

/* AVAILABLE (RED) */
.text-danger {
  background: #fee2e2;
  color: #dc2626 !important;
  border: none !important;
}

/* AVAILABLE (GREEN actually booked) */
.text-success {
  background: #dcfce7;
  color: #16a34a !important;
  border: none !important;
}

/* BUTTON */
.btn-primary {
  width: 100%;
  border-radius: 8px;
  margin-top: 5px;
  font-size: 13px;
  background: #38bdf8;
  border: none;
}

.btn-primary:hover {
  background: #0ea5e9;
}

/* BACK BUTTON */
.col-1 {
  display: flex;
  justify-content: center;
  margin-top: 25px;
  width: 100%;          /* ⬅️ full width so it centers properly */
}

.btn-danger {
  border-radius: 10px;
  padding: 8px 20px;    /* ⬅️ thoda bada */
  font-size: 15px;      /* ⬅️ text thoda bada */
  font-weight: 500;
}
</style>