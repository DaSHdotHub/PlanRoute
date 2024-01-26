<template>
    <div class="container mt-4">
        <h2>Patient Details</h2>
        <form>
            <div class="mb-3">
                <label for="firstname" class="form-label">First Name</label>
                <input type="text" class="form-control" id="firstname" :value="patient.firstname" readonly>
            </div>
            <div class="mb-3">
                <label for="lastname" class="form-label">Last Name</label>
                <input type="text" class="form-control" id="lastname" :value="patient.lastname" readonly>
            </div>
            <div class="mb-3">
                <label for="gender" class="form-label">Gender</label>
                <input type="text" class="form-control" id="gender" :value="genderLabel(patient.gender)" readonly>
            </div>
            <div class="mb-3">
                <label for="birthdate" class="form-label">Birth Date</label>
                <input type="text" class="form-control" id="birthdate" :value="patient.birth_date" readonly>
            </div>
            <div class="mb-3">
                <label for="address" class="form-label">Address</label>
                <input type="text" class="form-control" id="address" :value="formatAddress(patient.address)" readonly>
            </div>
            <div class="mb-3">
                <label for="geo-info" class="form-label">Geo Information</label>
                <input type="text" class="form-control" id="geo" :value="formatGeo(patient.address)" readonly>
            </div>
            <div class="mb-3">
                <label for="last_editor" class="form-label">Edited by</label>
                <input type="text" class="form-control" id="last_editor" :value="formatEditor(patient.last_editor, patient.last_edited)" readonly>
            </div>
            <div class="mb-3">
                <label for="creator" class="form-label">Created by</label>
                <input type="text" class="form-control" id="creator" :value="formatCreator(patient.creator, patient.created_at)" readonly>
            </div>
            <!-- Add Back button -->
            <button type="button" class="btn btn-secondary" @click="goBack">Back</button>
        </form>
    </div>
</template>
  
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
            }
        };
    },
    async mounted() {
        const patientId = this.$route.params.id;
        await this.fetchPatientDetails(patientId);
    },
    methods: {
        async fetchPatientDetails(patientId) {
            try {
                axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL;
                const response = await axios.get('/api/patients/${patientId}/', {
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
            return address ? `${address.latitude} ${address.longitude}`: 'No Geo Information';
        },
        formatEditor(editor, edited) {
            return editor ? `Last edited on ${edited} by ${editor}`: 'No Editor Information';
            //TODO: Lookup editor in Users
        },
        formatCreator(creator, created) {
            return creator ? `Created on ${created} by ${creator}`: 'No Creator Information';
            //TODO: Lookup creator in Users
        },
        goBack() {
            this.$router.push({ name: 'Dashboard' })
        }
    }
};
</script>