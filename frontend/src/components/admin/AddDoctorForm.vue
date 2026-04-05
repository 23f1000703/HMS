<template>
  <div>
    <h3>Add New Doctor</h3>

    <input v-model="name" placeholder="Full Name" />
    <input v-model="specialization" placeholder="Specialization" />
    <input v-model="experience" placeholder="Experience" />

    <button @click="addDoctor">Create</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      specialization: '',
      experience: ''
    }
  },
  methods: {
    addDoctor() {
      console.log(this.name, this.specialization, this.experience)
    }
  }
}
</script>