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

<style scoped>
.department-container h2 {
  text-align: center;
}
.department-container { padding: 25px; } /* HEADING */ .department-container h2 { font-weight: 600; color: #1e293b; margin-bottom: 20px; } /* OUTER BOX */ .dept-box { background: #ffffff; border-radius: 12px; padding: 15px; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08); } /* EACH ROW */ .dept-row { display: flex; justify-content: space-between; align-items: center; padding: 15px 18px; margin-bottom: 10px; border-radius: 10px; background: #f1f5f9; transition: 0.3s; } /* HOVER EFFECT */ .dept-row:hover { background: #e2e8f0; transform: translateY(-2px); } /* NAME */ .dept-name { font-size: 18px; font-weight: 500; color: #0f172a; } /* BUTTON */ .view-btn { padding: 6px 14px; border-radius: 8px; border: none; background: #38bdf8; color: white; font-size: 14px; transition: 0.3s; } .view-btn:hover { background: #0ea5e9; }
</style>