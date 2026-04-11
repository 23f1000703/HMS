<script setup >
import { ref } from 'vue'
import { useRouter } from 'vue-router'


const router = useRouter()

const role = localStorage.getItem("role")
const userID =Number(localStorage.getItem("patId"))
const DocId =Number(localStorage.getItem("docId"))
console.log("avi jo nikala",userID)


const Appoints = ref([])
const userAppoints = ref([])
const DoctorAppoints =ref([])
async function getyourAppointments() {
const response = await fetch('http://127.0.0.1:5000/api/patappointments',{
          })
        const result = await response.json()
        Appoints.value = result
        userAppoints.value = result.filter(a => a.patient_id == userID)
        DoctorAppoints.value = result.filter(b => b.doctor_id == DocId)
        console.log('apppoinment',Appoints.value)
        console.log('docappoint',DoctorAppoints.value)
      }

getyourAppointments()



async function Complete(id){
  const response = await fetch('http://127.0.0.1:5000/api/comp', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
          body: JSON.stringify({
      id: id})
    })
    getyourAppointments()
}

async function Cancel(id){
  const response = await fetch(`http://127.0.0.1:5000/api/deleteappoint/${id}`,{ 
    method : 'DELETE'
}) 
getyourAppointments()
}

function updatePatient(id,docId,patId) {
  router.push(`/updatepat/${id}/${docId}/${patId}`)
}
function Pathis(doc,pat) {
  router.push(`pathistory/${doc}/${pat}`)
}

</script>
<template>
  <div>
    <h3>Upcoming Appointments</h3>
    <div v-if = "role === 'admin'">

    <table class="table table-bordered w-100 mt-2 text-center">
      <tr>
        <th>Sr no.</th>
        <th>Patient Name</th>
        <th>Doctor Name</th>
        <th>Department</th>
        <th>Patient history</th>
      </tr>

      <tr v-for="a in Appoints" :key="a.id">
        <td>{{ a.id }}</td>
        <td>{{ a.patient }}</td>
        <td>{{ a.doctor }}</td>
        <td>{{ a.dept }}</td>
        <td><a class="btn btn-secondary" @click ="Pathis(a.doctor_id,a.patient_id)">View</a></td>
      </tr>
    </table>
  </div>

  <div v-if = "role === 'doctor'">

    <table class="table table-bordered w-100 mt-2 text-center">
      <tr>
        <th>Sr no.</th>
        <th>Patient Name</th>
        <th>Patient History</th>
        <th>Completed</th>
        <th>Cancel</th>
        
      </tr>

      <tr v-for="a in DoctorAppoints" :key="a.id">
        <td>{{ a.id }}</td>
        <td text-uppercase>{{ a.patient }}</td>
        <td><button class="btn btn-secondary"@click="updatePatient(a.id,a.doctor_id,a.patient_id)">Update</button></td>
        <td><button class="btn btn-secondary"@click= "Complete(a.id)">Mark as complete</button></td>
        <td><a class="btn btn-secondary"  @click="Cancel(a.id)">Cancel</a></td>
      </tr>
    </table>
    </div>
    <div v-if = "role === 'patient'">
    <table class="table table-bordered w-100 mt-2 text-center">
       <thead>    
      <tr>
        <th>Sr no.</th>
        <th>Doctor Name</th>
        <th>Department</th>
        <th>Date</th>
        <th>Time</th>
        <th>Cancel</th>
        
      </tr>
      </thead>

      <tbody>
      <tr v-for="a in userAppoints" :key="a.id">
        
        <td>{{ a.id }}</td>
        <td text-uppercase>{{ a.doctor }}</td>
        <td text-uppercase>{{ a.dept }}</td>
        <td text-uppercase>{{ a.Date.slice(0, 16) }}</td>
        <td text-uppercase>{{ a.time === 'evening' ? '04:00 - 09:00 PM' : '08:00 - 12:00 AM' }}</td>
        <td><a class="btn btn-secondary " @click="Cancel(a.id)">Cancel</a></td>
      </tr>
      
      </tbody>
    </table>

    </div>
  </div>
</template>

