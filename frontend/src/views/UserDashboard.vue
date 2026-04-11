<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import AdminHeader from '@/components/admin/Adminheader.vue'
import AppointmentTable from '@/components/admin/AppointmentTable.vue'
import PatientRecord from '@/components/PatientRecord.vue'

const router = useRouter()
const doc = [
  "Cardiologist",
  "Neurologist",
  "Orthopedic",
  "Dermatologist"
]
const Id = localStorage.getItem("user_id")
const role = localStorage.getItem("role")

console.log('Id and role',Id,role)
const Appoint = ref([])
const userId = ref('')
const userName =ref('')
async function usersId() {
  const response =await fetch('http://127.0.0.1:5000/api/userid',{
    method:'POST',
    headers:{
      'content-type':'application/json'
    },
    body:JSON.stringify({Id:Id,role:role}) 
  })
  const result = await response.json()
  userId.value =result
  if (role === 'doctor') {
    userId.value = result.doc_id
    userName.value = result.name

    localStorage.setItem('docId', result.doc_id)
    localStorage.setItem('docName', result.name)
  }

  else if (role === 'patient') {
    userId.value = result.pat_id
    userName.value = result.name

    localStorage.setItem('patId', result.pat_id)
    localStorage.setItem('patName', result.name)
  }
}

async function getAppointments() {
const response = await fetch('http://127.0.0.1:5000/api/patappointments',{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({Id: Id,role:role})
        });
        const result = await response.json()
        Appoint.value = result
        console.log('user ka Appoint',Appoint.value)
      }
getAppointments()
usersId()

function viewDepartment(dept) {
  router.push(`/department/${dept}`)
}
</script>

<template>
    <Navbar />

    <AdminHeader :docname="'null' " :patname="userName"/>

    <div class="department-container">
    <h2>Departments</h2>

    <div class="dept-box">
      <div class="dept-row" v-for="dept in doc" :key="dept">
        <span class="dept-name">{{ dept }}</span>
        <button class="view-btn" @click="viewDepartment(dept)">view details</button>
      </div>
    </div>
  </div>
  <AppointmentTable />
    
</template>

<style>
.department-container {
  padding: 20px;
}

/* outer box */
.dept-box {
  border: 2px solid black;
  padding: 15px;
}

/* each row */
.dept-row {
  display: flex;
  justify-content: space-between;
  align-items: center;

  border: 1px solid gray;
  padding: 15px;
  margin-bottom: 10px;
}

/* department name */
.dept-name {
  font-size: 20px;
}

/* button */
.view-btn {
  padding: 8px 15px;
  border-radius: 10px;
  border: 2px solid blue;
  background-color: lightblue;
  cursor: pointer;
}
</style>