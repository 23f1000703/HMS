<script setup>
import { ref } from 'vue'
import Navbar from '../../components/Navbar.vue'
import AdminHeader from '../../components/admin/Adminheader.vue'
import UserList from '../../components/admin/UserList.vue'
import AppointmentTable from '../../components/admin/AppointmentTable.vue'


const doctors = ref([])
const patients =ref([])


async function fetchDoctors() {
  const response = await fetch('http://127.0.0.1:5000/api/doclist')
  const data = await response.json()

  console.log("DATA:", data)

  doctors.value = data

}

async function fetchpatient() {
  const response = await fetch('http://127.0.0.1:5000/api/patlist')
  const patdata = await response.json()

  console.log('Pat data',patdata)

  patients.value = patdata
}
fetchDoctors()
fetchpatient()
</script>

<template>

  <Navbar />

  <AdminHeader />
  
  <UserList :users="doctors" title="Registered Doctors" />
  <UserList :users="patients" title="Registered Patients" />

  <AppointmentTable />

</template>