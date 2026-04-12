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

function Back(){
  router.back()
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
    <button @click ="Back">Back</button>
  </div>
</template>

<style scoped>
/* HEADER */
.header {
  padding: 25px;
  margin-bottom: 20px;
  width: 100%;              /* ⬅️ full width */
}

/* MAIN TITLE */
.header h1 {
  font-size: 30px;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 15px;
}

/* SECTION (BOTH BOX SAME WIDTH) */
.section {
  background: #ffffff;
  padding: 20px 22px;
  border-radius: 12px;
  margin-bottom: 20px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.08);

  width: 100%;              /* ⬅️ full width */
}

/* SECTION TITLE */
.section h2 {
  font-size: 21px;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 10px;
}

/* TEXT */
.section p {
  font-size: 14px;
  color: #475569;
  line-height: 1.6;
  font-weight: 500;
}

/* DOCTOR ROW */
.section div[v-for] {
  display: flex;
  justify-content: space-between;
  align-items: center;

  background: #f1f5f9;
  padding: 14px 18px;
  margin-bottom: 10px;
  border-radius: 10px;
  transition: 0.25s;
}

/* HOVER */
.section div[v-for]:hover {
  background: #e2e8f0;
  transform: translateY(-2px);
}

/* NAME */
.name {
  font-size: 17px;
  font-weight: 600;
  color: #0f172a;
}

/* ACTION BUTTONS */
.actions {
  display: flex;
  gap: 10px;
}

/* BUTTON BASE */
.actions button {
  border: none;
  border-radius: 8px;
  padding: 6px 12px;
  font-size: 13px;
  cursor: pointer;
  transition: 0.25s;
}

/* CHECK */
.actions button:first-child {
  background: #38bdf8;
  color: white;
}

.actions button:first-child:hover {
  background: #0ea5e9;
}

/* VIEW */
.actions button:last-child {
  background: #64748b;
  color: white;
}

.actions button:last-child:hover {
  background: #475569;
}

/* BACK BUTTON */
button {
  margin-top: 15px;
  padding: 6px 14px;
  border-radius: 8px;
  border: none;
  background: #facc15;
  color: #1e293b;
  font-weight: 500;
}

button:hover {
  background: #eab308;
}
</style>
