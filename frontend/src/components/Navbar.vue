<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const role = localStorage.getItem("role")
console.log(role)

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
      router.push('/login')
    }
  }

</script>

<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand">Hospital Management System</a>

      <div v-if=" role === 'patient'">
        <RouterLink to="/pathhistory">Edit</RouterLink>
        |
        <RouterLink to="/pathistory">History</RouterLink>
        |
      </div>
      
      <button @click="logout">Logout</button>
    </div>
</nav>
</template>



