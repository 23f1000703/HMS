<script setup>
import { ref } from 'vue'
import Navbar from '@/components/Navbar.vue'
import AdminHeader from '@/components/admin/Adminheader.vue'
import AppointmentTable from '@/components/admin/AppointmentTable.vue'
import { useRoute, useRouter } from 'vue-router'

const Router = useRouter()
const Route = useRoute()
const Id = localStorage.getItem("user_id")
const role = localStorage.getItem("role")
const docId = localStorage.getItem('docId')

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

const Appoint = ref('')
async function getAppointments() {
const response = await fetch('http://127.0.0.1:5000/api/patappointments',{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({Id: Id,role:role})
        });
          const result = await response.json()
          console.log('Result',result)
          const unique = []
          const seen = []

          for (const item of result) {
            if (!seen.includes(item.pat_id)) {
              seen.push(item.pat_id)
              unique.push(item)
         }
       }
        Appoint.value = unique
        console.log('unique',Appoint.value)
      }

getAppointments()
usersId()
function View(docid,patid){
  Router.push(`/pathistory/${docid}/${patid}`)
}
function Available(docid,patid){
  Router.push(`/docavail/${docid}/${patid}`)
}

</script>

<template>
    <Navbar />
    <AdminHeader :docname="userName" :patname="'null'" />
    <AppointmentTable />
    <div class="container mt-4">

    <h2 class="mb-3">Assigned Patient</h2>

    <div class="border p-3 rounded">

      <div v-for="user in Appoint" :key="user.id"
        class="d-flex justify-content-between align-items-center border p-1 mb-1 rounded">

        <span class="fs-7 text-secondary">
          {{ user.name }}
        </span>

        <div>
          <button class="btn btn-warning me-2" @click="View(user.doc_id,user.pat_id)">View</button>
        </div>
      </div>

    </div>
  </div>

  <div class="container text-end mt-4">
    <button class="btn btn-success px-4" @click ="Available(docId,pat_id)">Provide Availability</button>
  </div>

</template>