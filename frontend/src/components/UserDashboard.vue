<template>
    <div class="container mt-4">
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
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        patients: []
      };
    },
    mounted() {
      this.fetchPatients();
    },
    methods: {
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
  