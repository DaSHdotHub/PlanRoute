<template>
    <div class="container mt-4">
      <h1 class="mb-4">Patient List</h1>
      <div v-if="loading" class="text-center">
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
      <div v-else>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Name</th>
              <th scope="col">Gender</th>
              <th scope="col">Birth Date</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(patient, index) in patients" :key="patient.id">
              <th scope="row">{{ index + 1 }}</th>
              <td>{{ patient.firstname }} {{ patient.lastname }}</td>
              <td>{{ patient.gender }}</td>
              <td>{{ patient.birth_date }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        patients: [],
        loading: false,
      };
    },
    mounted() {
      this.fetchPatients();
    },
    methods: {
      async fetchPatients() {
        this.loading = true;
        try {
          const response = await axios.get('http://127.0.0.1:8000/core/patients/');
          this.patients = response.data;
        } catch (error) {
          console.error('There was an error fetching the patients:', error);
        } finally {
          this.loading = false;
        }
      },
    },
  };
  </script>
  
  <style>
  </style>