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


function goToHistory(patid){
  router.push(`/patfullrec/${patid}`)
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
        <button @click="goToHistory(patId)">History</button>
        |
      </div>
      
      <button @click="logout">Logout</button>
    </div>
</nav>
</template>

<style scoped>
/* NAVBAR BASE */
.navbar {
  background: #6b7c85 !important;
  padding: 12px 24px;
  border-bottom: 1px solid #5a6b73;
  box-shadow: 0 3px 10px rgba(0,0,0,0.15);
}

/* FLEX ALIGN */
.container-fluid {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* BRAND */
.navbar-brand {
  color: #ffffff !important;
  font-weight: 600;
  font-size: 20px;
  letter-spacing: 0.5px;
}

/* BUTTON BASE */
button {
  border: none;
  border-radius: 8px;
  padding: 6px 14px;
  font-size: 14px;
  font-weight: 500;
  margin: 0 5px;
  cursor: pointer;
  transition: 0.25s;
}

/* ACTION GROUP (Edit + History) */
div[v-if] {
  display: flex;
  align-items: center;
}

/* 🟡 EDIT & HISTORY */
button:nth-of-type(1),
button:nth-of-type(2) {
  background: #facc15;
  color: #1e293b;
}

button:nth-of-type(1):hover,
button:nth-of-type(2):hover {
  background: #eab308;
  transform: translateY(-1px);
}

/* 🔴 LOGOUT */
button:last-child {
  background: #ef4444;
  color: white;
}

button:last-child:hover {
  background: #dc2626;
  transform: translateY(-1px);
}

/* SEPARATOR "|" STYLE */
div[v-if] {
  gap: 6px;
}

/* REMOVE "|" DEFAULT LOOK */
div[v-if]::before,
div[v-if]::after {
  content: "";
}
</style>


