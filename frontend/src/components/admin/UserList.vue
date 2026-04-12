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
        
        <span class="fs-7 text-secondary">
          {{ user.specialization }}
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

<style scoped>
/* MAIN CONTAINER */
.container {
  width: 100%;
  margin: 25px 0;
  padding: 0 20px;
}

/* HEADING */
h2 {
  text-align: center;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 18px;
}

/* OUTER BOX */
.container > .border {
  background: #ffffff;
  padding: 18px;
  border-radius: 12px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.08);
  border: none !important;
}

/* EACH USER ROW */
.container .d-flex {
  padding: 12px 16px;
  margin-bottom: 10px;
  border-radius: 8px;
  background: #f1f5f9;
  transition: 0.25s;
}

/* HOVER EFFECT */
.container .d-flex:hover {
  background: #e2e8f0;
  transform: translateY(-1px);
}

/* USER NAME */
.fs-7 {
  font-size: 15px !important;
  font-weight: 500;
  color: #1e293b !important;
}

/* BUTTON BASE */
.btn {
  border-radius: 8px;
  padding: 5px 12px;
  font-size: 13px;
  transition: 0.25s;
}

/* EDIT (YELLOW) */
.btn-warning {
  background: #facc15;
  border: none;
  color: #1e293b;
}

.btn-warning:hover {
  background: #eab308;
}

/* DELETE (RED) */
.btn-danger {
  background: #ef4444;
  border: none;
}

.btn-danger:hover {
  background: #dc2626;
}

/* BLACKLIST / UNBLOCK (GREY) */
.btn-secondary {
  background: #64748b;
  border: none;
}

.btn-secondary:hover {
  background: #475569;
}
</style>