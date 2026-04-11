<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

const { users, title } = defineProps(['users', 'title'])

async function Blacklist(id){
  const response = await fetch('http://127.0.0.1:5000/api/blacklist',{ 
    method : 'PUT',
    headers :{ 'Content-type':'application/json'},
    body:JSON.stringify({user_id:id})
})
   const result = await response.json()
   if(response.ok){
    alert(result.message)
  } else {
    alert("Error: " + result.message)
  }
  window.location.reload()
}

async function Delete(id){
  const response = await fetch(`http://127.0.0.1:5000/api/delete/${id}`,{ 
    method : 'DELETE'
})

 const result=await response.json()
 alert(result.message)
 window.location.reload()
}

function Editdoc(useId) {
  router.push(`/docedit/${useId}`)
}
function Editpat(id) {
  router.push(`/patedit/${id}`)
}
</script>

<template>
  <div class="container mt-4">
    <h2 class="mb-3">{{ title }}</h2>
    <div class="border p-3 rounded">
      <div 
        v-for="user in users" :key="user.id"
        class="d-flex justify-content-between align-items-center border p-1 mb-1 rounded">

        <span class="fs-7 text-secondary">
          {{ user.name }}
        </span>
        <div>
          <button class="btn btn-warning me-2"@click='user.address ? Editpat(user.user_id) : Editdoc(user.id)'>edit</button>
          <button class="btn btn-danger me-2"@click='Delete(user.user_id)'>delete</button>
          <button class="btn btn-secondary"@click = 'Blacklist(user.user_id)'>{{ user.active ? 'Blacklist' : 'Unblock' }}</button>
        </div>
      </div>

    </div>
  </div>
</template>