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

<style scoped>
/* PAGE SPACING */
:deep(.navbar) {
  margin-bottom: 10px;
}

/* SECTION SPACING */
:deep(.container),
:deep(.container-fluid) {
  padding: 0 25px;
}

/* USER LIST SECTION */
:deep(.user-list-container) {
  background: #ffffff;
  padding: 18px;
  border-radius: 12px;
  margin-bottom: 20px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

/* SECTION TITLE */
:deep(h2),
:deep(h3) {
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 15px;
}

/* APPOINTMENT TABLE WRAPPER */
:deep(.table) {
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

/* CARD LIKE SECTIONS */
:deep(.card-section) {
  background: #ffffff;
  padding: 20px;
  border-radius: 12px;
  margin-bottom: 20px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

/* HOVER EFFECT FOR LIST ITEMS */
:deep(.list-item:hover) {
  background: #f1f5f9;
}

/* GLOBAL BUTTON POLISH */
:deep(.btn) {
  border-radius: 8px;
  font-size: 14px;
}

/* SMALL SPACING BETWEEN COMPONENTS */
:deep(.component-gap) {
  margin-bottom: 20px;
}
</style>