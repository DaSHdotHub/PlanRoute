<template>
    <div class="container mt-4">
        <h2>Patient Details</h2>
        <form @submit.prevent="updatePatient">
            <div class="mb-3">
                <label for="firstname" class="form-label">First Name</label>
                <input type="text" class="form-control" :class="{ 'changed-field': fieldChanged('firstname') }"
                    id="firstname" v-model="patient.firstname">
            </div>
            <div class="mb-3">
                <label for="lastname" class="form-label">Last Name</label>
                <input type="text" class="form-control" :class="{ 'changed-field': fieldChanged('lastname') }" id="lastname"
                    v-model="patient.lastname" readonly>
            </div>
            <div class="mb-3">
                <label for="gender" class="form-label">Gender</label>
                <select class="form-control" id="gender" v-model="patient.gender">
                    <option value="">Select Gender</option>
                    <option value="M">Male</option>
                    <option value="F">Female</option>
                    <option value="O">Other</option>
                    <option value="U">Prefer not to say</option>
                </select>
            </div>
            <div class="mb-3">
                <label for="birthdate" class="form-label">Birth Date</label>
                <input type="text" class="form-control" :class="{ 'changed-field': fieldChanged('birth_date') }"
                    id="birthdate" v-model="patient.birth_date">
            </div>
            <div class="mb-3">
                <label for="street" class="form-label">Street</label>
                <input type="text" class="form-control" :class="{ 'changed-field': fieldChanged('street') }"
                id="street" v-model="patient.address.street">
            </div>
            <div class="mb-3">
                <label for="zip_code" class="form-label">Street</label>
                <input type="text" class="form-control" :class="{ 'changed-field': fieldChanged('street_number') }"
                id="zip_code" v-model="patient.address.street_number">
            </div>
            <div class="mb-3">
                <label for="city" class="form-label">Street</label>
                <input type="text" class="form-control" :class="{ 'changed-field': fieldChanged('zip_code') }"
                id="city" v-model="patient.address.zip_code">
            </div>
            <div class="mb-3">
                <label for="street" class="form-label">Street</label>
                <input type="text" class="form-control" :class="{ 'changed-field': fieldChanged('city') }"
                id="street" v-model="patient.address.city">
            </div>
            <div class="mb-3">
                <label for="geo-info" class="form-label">Geo Information</label>
                <input type="text" class="form-control" id="geo" :value="formatGeo(patient.address)" readonly>
            </div>
            <div class="mb-3">
                <label for="last_editor" class="form-label">Edited by</label>
                <input type="text" class="form-control" id="last_editor"
                    :value="formatEditor(patient.last_editor, patient.last_edited)" readonly>
            </div>
            <div class="mb-3">
                <label for="creator" class="form-label">Created by</label>
                <input type="text" class="form-control" id="creator"
                    :value="formatCreator(patient.creator, patient.created_at)" readonly>
            </div>
            <!-- Confirmation Button -->
            <button type="submit" class="btn btn-primary">Confirm</button>
            <!-- Back Button -->
            <button type="button" class="btn btn-secondary" @click="goBack">Back</button>
        </form>
    </div>
</template>

<style>
.changed-field {
    background-color: lightgreen;
}
</style>
  
<script>
import axios from 'axios';
export default {
    data() {
        return {
            patient: {
                firstname: 'Not yet loaded',
                lastname: 'Not yet loaded',
                gender: 'Not yet loaded',
                birth_date: 'Not yet loaded',
                address: 'Not yet loaded',
                geo: 'Not yet loaded',
                last_editor: 'Not yet loaded',
                creator: 'Not yet loaded',
            },
            originalPatient: {}
        };
    },
    async mounted() {
        const patientId = this.$route.params.id;
        await this.fetchPatientDetails(patientId);
        this.originalPatient = JSON.parse(JSON.stringify(this.patient));
    },
    methods: {
        async updatePatient() {
            try {
                // TODO Validation or Restriction
                const response = await axios.put(`http://127.0.0.1:8000/api/patients/${this.patient.id}/`, this.patient, {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('access_token')}`
                    }
                });
                console.log("Patient updated:", response.data);
                // TODO: Handle successful update
            } catch (error) {
                console.error('Error updating patient:', error);
                // TODO: Handle error
            }
        },
        fieldChanged(fieldName) {
            return this.patient[fieldName] !== this.originalPatient[fieldName];
        },
        // ... other methods ...
    },
    async fetchPatientDetails(patientId) {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/patients/${patientId}/`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('access_token')}`
                }
            });
            this.patient = response.data;
        } catch (error) {
            console.error('Error fetching patient details:', error);
            // TODO: Handle error
        }
    },
    genderLabel(genderCode) {
        const genderMap = { 'M': 'Male', 'F': 'Female', 'O': 'Other', 'U': 'Prefer not to say' };
        return genderMap[genderCode] || 'Unknown';
    },
    formatAddress(address) {
        return address ? `${address.street} ${address.street_number}, ${address.zip_code} ${address.city}` : 'No Address';
    },
    formatGeo(address) {
        return address ? `${address.latitude} ${address.longitude}` : 'No Geo Information';
    },
    formatEditor(editor, edited) {
        return editor ? `Last edited on ${edited} by ${editor}` : 'No Editor Information';
        //TODO: Lookup editor in Users
    },
    formatCreator(creator, created) {
        return creator ? `Created on ${created} by ${creator}` : 'No Creator Information';
        //TODO: Lookup creator in Users
    },
    goBack() {
        this.$router.push({ name: 'Dashboard' })
    }
};
</script>