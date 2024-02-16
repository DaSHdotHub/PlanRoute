<template>
    <div>
      <b-container class="bv-example-row">
        <h2>Edit Patient Details</h2>
        <b-form @submit.prevent="savePatient">
          <!-- Editable Fields -->
          <b-form-group label="First Name" label-for="firstname">
            <b-form-input id="firstname" v-model="patientData.firstname"></b-form-input>
          </b-form-group>
  
          <b-form-group label="Last Name" label-for="lastname">
            <b-form-input id="lastname" v-model="patientData.lastname"></b-form-input>
          </b-form-group>
  
          <b-form-group label="Birth Date" label-for="birth_date">
            <b-form-input id="birth_date" type="date" v-model="patientData.birth_date"></b-form-input>
          </b-form-group>
  
          <!-- Read-only Fields -->
          <b-form-group label="ID" label-for="id">
            <b-form-input id="id" readonly :value="patientData.id"></b-form-input>
          </b-form-group>
  
          <b-form-group label="Latitude" label-for="latitude">
            <b-form-input id="latitude" readonly :value="patientData.address.latitude"></b-form-input>
          </b-form-group>
  
          <b-form-group label="Longitude" label-for="longitude">
            <b-form-input id="longitude" readonly :value="patientData.address.longitude"></b-form-input>
          </b-form-group>
  
          <b-form-group label="Creator" label-for="creator">
            <b-form-input id="creator" readonly :value="patientData.creator"></b-form-input>
          </b-form-group>
  
          <b-form-group label="Last Editor" label-for="last_editor">
            <b-form-input id="last_editor" readonly :value="patientData.last_editor"></b-form-input>
          </b-form-group>
  
          <!-- Action Buttons -->
          <b-button variant="primary" class="me-2" type="submit">Save</b-button>
          <b-button variant="secondary" @click="exitWithoutSaving">Exit</b-button>
        </b-form>
      </b-container>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  export default {
    props: {
      patientId: Number,
    },
    setup(props) {
      const router = useRouter();
  
      // Replace with actual fetching logic
      const patientData = ref({
        id: props.patientId,
        firstname: 'Max',
        lastname: 'Mustermann',
        birth_date: '1990-10-10',
        address: {
          latitude: 52.35804,
          longitude: 9.66831,
        },
        creator: 'Admin',
        last_editor: 'Admin',
      });
  
      const savePatient = () => {
        // Implement saving logic here
        router.push({ name: 'Dashboard' });
      };
  
      const exitWithoutSaving = () => {
        router.push({ name: 'Dashboard' }); 
      };
  
      return { patientData, savePatient, exitWithoutSaving };
    },
  };
  </script>
  
  <style scoped>
  .bv-example-row {
    margin-top: 20px;
  }
  </style>