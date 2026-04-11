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

/* Overall container */
div {
  max-width: 700px;
  margin: 20px auto;
}

/* Row layout */
.row {
  align-items: center;
  margin-bottom: 8px;
}

/* Date */
.col-3 {
  font-size: 13px;
  font-weight: 500;
  color: #374151;
}

/* Slot box (small & clean) */
.col-4 span {
  display: inline-block;
  width: 100%;
  text-align: center;
  padding: 6px 8px;
  font-size: 13px;
  border-radius: 6px;
  border: 1px solid;
  transition: all 0.15s ease;
}

/* Available (green - subtle) */
.text-success {
  background-color: #f0fdf4;
  color: #15803d !important;
  border-color: #bbf7d0;
}

/* Booked (red - subtle) */
.text-danger {
  background-color: #fef2f2;
  color: #b91c1c !important;
  border-color: #fecaca;
}

/* Hover (very light) */
.col-4 span:hover {
  opacity: 0.85;
  cursor: pointer;
}

</style>