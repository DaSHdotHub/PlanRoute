// stores/patientsStore.js
import { defineStore } from 'pinia';
import apiClient from '../axios';

export const usePatientsStore = defineStore('patients', {
    state: () => ({
        patients: [],
        addresses: [],
    }),
    getters: {
        getPatientById: (state) => (id) => {
            return state.patients.find((patient) => patient.id === id);
        },
    },
    actions: {
        async updatePatient(patientData) {
            try {
                const response = await apiClient.put(`/api/patients/${patientData.id}/`, patientData);
                // Update the local patient data with the response, if necessary
                const index = this.patients.findIndex((patient) => patient.id === patientData.id);
                if (index !== -1) {
                    this.patients[index] = response.data;
                }
                console.log("Patient updated:", response.data);
            } catch (error) {
                console.error('Error updating patient:', error);
                // Handle error
            }
        },
        async fetchPatient(patientId) {
            try {
                const response = await apiClient.get(`/api/patients/${patientId}`);
                this.patients = [response.data];
            } catch (error) {
                console.error('Error fetching patient:', error);
                // Handle error, e.g., by setting an error state
            }
        },
        async fetchAllPatients() {
            try {
                const response = await apiClient.get('/api/patients/');
                this.patients = response.data;
            } catch (error) {
                console.error('Error fetching all patients:', error);
            }
        },
        async fetchAddress(addressId) {
            try {
                const response = await apiClient.get(`/api/addresses/${addressId}`);
                this.addresses = [response.data];
            } catch (error) {
                console.error('Error fetching address:', error);
                // Handle error
            }
        },
        async fetchAllAddresses() {
            try {
                const response = await apiClient.get('/api/addresses/');
                this.addresses = response.data;
            } catch (error) {
                console.error('Error fetching all addresses:', error);
            }
        },
    },
});