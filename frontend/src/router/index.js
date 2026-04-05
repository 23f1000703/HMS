import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue'),
    },    
    {
      path: '/patientregister',
      name: 'patientregister',
      component: () => import('../views/patient_register.vue'),
    },
    { path: '/doctorregister',
      name: 'doctorregister',
      component: () => import('../components/admin/Doctor_register.vue')
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/admin/AdminDashboard.vue')
    },
    {
      path: '/patient',
      name: 'user',
      component: () => import('../views/UserDashboard.vue')
    },
    {
      path: '/doctor',
      name: 'doctor',
      component: () => import('../views/UserDashboard.vue')
    },
    {
      path: '/pathistory',
      name: 'pathistory',
      component: () => import('../components/Patient_history.vue')
    },
    {
      path: '/department',
      name: 'Department',
      component: () => import('../components/Department.vue')
    }
  ]
})

export default router