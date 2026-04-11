<script setup>
import { useRoute,useRouter } from 'vue-router'
import {ref, onMounted} from 'vue'
import Navbar from './Navbar.vue';

const router = useRouter()
const route = useRoute()
const docid = localStorage.getItem('docId')
const patid =localStorage.getItem('patId')
console.log('doc',docid,patid)

const Department = route.params.dept
console.log(Department)
const doc = ref([]) 
async function getDoctors() {
    const response = await fetch("http://127.0.0.1:5000/api/doclist",{
    method : 'GET',
    });
    const data = await response.json()
    doc.value = data;
    console.log("Data loaded:", doc.value);
}
onMounted(() => {
    getDoctors();
});


function goToHistory() {
  router.push('/history')
}

function logout() {
  localStorage.removeItem('token')
  router.push('/login')
}

function checkAvailability(docid,patid) {
  router.push(`/docavail/${docid}/${patid}`)
}

function viewDetails(id) {
  router.push(`/qual/${id}`)
}
</script>

<template>
  <Navbar />
  <div>
      <div v-if = "Department ==='Cardiologist' ">
        <div class="header">
          <h1>Department of Cardiology</h1>

          <div class="section">
            <h2>Overview</h2>
            <p><b>
              The Cardiology Department in a hospital is dedicated to the diagnosis, 
              treatment, and prevention of heart diseases and cardiovascular conditions. 
              It houses a team of specialized doctors, such as interventional cardiologists, 
              electrophysiologists, and cardiac surgeons, who work together to provide 
              comprehensive care for heart-related ailments, ranging from hypertension 
              to complex heart surgeries.
            </b></p>
          </div>
        </div>
      </div>

      <div v-if = "Department ==='Dermatologist' ">
        <div class="header">
          <h1>Department of Dermatology</h1>

          <div class="section">
            <h2>Overview</h2>
            <p>
             The Dermatology Department provides a holistic approach to skin, hair, 
             and nail health through a blend of medical, surgical, and aesthetic expertise. 
             Our Dermatologists and Dermatosurgeons are experts in treating chronic 
             inflammatory conditions such as psoriasis, vitiligo, and severe eczema, 
             as well as infectious skin diseases. Additionally, the department offers 
             specialized procedures for skin cancer screening, hair restoration, and 
             laser-based cosmetic enhancements. By combining clinical precision with 
             the latest dermatological research, we aim to provide effective solutions 
             for both pathological and aesthetic concerns.
            </p>
          </div>
        </div>
      </div>

      <div v-if ="Department ==='Neurologist' ">
        <div class="header">
          <h1>Department of Neurology</h1>

          <div class="section">
            <h2>Overview</h2>
            <p>
               The Neurology Department stands at the forefront of treating complex 
               disorders of the central and peripheral nervous systems. Our team, 
               consisting of world-class Neurologists and Neurosurgeons, specializes
                in the treatment of stroke, epilepsy, Parkinson's disease, and 
                neurodegenerative conditions like Alzheimer's. Equipped with high-resolution
                MRI and CT imaging, the department provides critical care for traumatic brain
                injuries and spinal cord disorders. We focus on integrating medical management
                with neuro-rehabilitation to help patients regain cognitive and motor functions
                 effectively.
            </p>
          </div>
        </div>
      </div>

      <div v-if = "Department ==='Orthopedic' ">
        <div class="header">
          <h1>Department of Orthopedic</h1>

          <div class="section">
            <h2>Overview</h2>
            <p>
              The Orthopedics Department offers expert surgical and non-surgical care for the 
              entire musculoskeletal system, including bones, joints, ligaments, tendons, and 
              muscles. Led by renowned Orthopedic Surgeons and Sports Medicine specialists, 
              the department handles a high volume of cases ranging from simple fractures and 
              ligament tears (ACL/MCL) to advanced robotic-assisted total hip and knee replacements. 
              With a dedicated wing for Physiotherapy and Rehabilitation, we ensure that patients—from 
              professional athletes to the elderly—receive the necessary support to restore their 
              mobility, strength, and quality of life.
            </p>
          </div>
        </div>
      </div>
  </div>

  <div class="section">
      <h2>Doctors' list</h2>
      <div v-for="special in doc" :key="special.id">
    
        <div v-if = "special.specialization === Department" >
            <span class="name">{{ special.name }}</span>
            <div class="actions">
              <button @click="checkAvailability(special.id,patid)">
                check availability
              </button>
              <button @click="viewDetails(special.id)">
                view details
              </button>
            </div>
        </div>

    </div>
  </div>
</template>

