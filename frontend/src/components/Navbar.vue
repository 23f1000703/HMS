<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const patId=localStorage.getItem("patId")
const useId =localStorage.getItem("user_id")
console.log(useId)
const role = localStorage.getItem("role")


    async function logout(){
      const token  = localStorage.getItem("token")
      console.log(token)
      const response = await fetch('http://127.0.0.1:5000/api/logout',{
      method : "POST",
      headers : {
        'Content-Type': 'application/json',
        "Authorization": token
      }
    }
    )
    console.log(response)
    if (response.ok){
      localStorage.clear()
      router.push('/login')
    }
  }


function goToHistory(docid,patid){
  router.push(`/pathistory/${docid}/${patid}`)
}
function Edit(id){
  router.push(`/patedit/${id}`)
}
console.log("Navbar",patId,role)
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand">Hospital Management System</a>

      <div v-if=" role === 'patient'">
        <button @click="Edit(useId)">Edit</button>
        |
        <button @click="goToHistory(docId,patId)">History</button>
        |
      </div>
      
      <button @click="logout">Logout</button>
    </div>
</nav>
</template>



