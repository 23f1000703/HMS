<template>
  <div>
    <h3>Upcoming Appointments</h3>

    <table class="table table-bordered w-100 mt-2 text-center">
      <tr>
        <th>Sr no.</th>
        <th>Patient Name</th>
        <th>Doctor Name</th>
        <th>Department</th>
        <th>Patient history</th>
      </tr>

      <tr v-for="a in appointments" :key="a.id">
        <td>{{ a.id }}</td>
        <td>{{ a.patient }}</td>
        <td>{{ a.doctor }}</td>
        <td>{{ a.dept }}</td>
        <td><a class="btn btn-secondary disabled" role="button" aria-disabled="true">View</a></td>
      </tr>
    </table>
  </div>
</template>

<script setup >

      const appointments =  [
        { id: 1, patient: "Mr. abc", doctor: "Dr. xyz", dept: "Cardiology" }
      ]
</script>