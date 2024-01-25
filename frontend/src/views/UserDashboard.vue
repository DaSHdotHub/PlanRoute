<template>
  <HeaderComponent />
  <div class="container mt-4">
    <button @click="logout">Logout</button>
    <h2>Dashboard</h2>
    <table class="table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Address</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="patient in patients" :key="patient.id">
          <td>{{ patient.id }}</td>
          <td>{{ patient.firstname }} {{ patient.lastname }}</td>
          <td>{{ formatAddress(patient.address) }}</td>
          <td>
            <b-icon icon="eye" @click="viewPatient(patient)" />
            <b-icon v-if="userCanEdit" icon="pencil" @click="editPatient(patient)" />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <FooterComponent />
</template>
  
<script>
import HeaderComponent from '@/components/shared/HeaderComponent.vue';
import FooterComponent from '@/components/shared/FooterComponent.vue';
import axios from 'axios';

export default {
  components: {
    HeaderComponent,
    FooterComponent
  },
  data() {
    return {
      patients: [],
      userCanEdit: false, // TODO: Check if user can edit
    };
  },
  mounted() {
    this.checkPermissions();
    this.fetchPatients();
  },
  methods: {
    logout() {
      localStorage.removeItem('access_token');
      delete axios.defaults.headers.common['Authorization'];
      this.$router.push({ name: 'Home' });
    },
    checkPermissions() {
      // Implement logic to check if the user is part of the crud_group
      // Set userCanEdit accordingly
    },
    viewPatient(patient) {
      this.$router.push({ name: 'ViewPatient', params: { id: patient.id } });
    },
    editPatient(patient) {
      this.$router.push({ name: 'EditPatient', params: { id: patient.id } });
    },
    async fetchPatients() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/patients/', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`
          }
        });
        this.patients = response.data;
      } catch (error) {
        console.error('Error fetching patients:', error);
        // TODO: Handle error
      }
    },
    formatAddress(address) {
      // TODO: Format address
      return address ? `${address.street} ${address.street_number}, ${address.zip_code}` : 'No Address';
    }
  }
};
</script>
  