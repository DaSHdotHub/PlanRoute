<template>
  <div>
    <HeaderComponent />
    <div class="dashboard-container">
      <button class="mdc-button logout-button" @click="logoutAction">
        Logout
      </button>
      <h2>Dashboard</h2>
      <div class="table-responsive">
        <table class="mdc-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Address</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="patient in patients" :key="patient.id">
              <td>{{ patient.id }}</td>
              <td>{{ patient.firstname }} {{ patient.lastname }}</td>
              <td>{{ formatAddress(patient.address) }}</td>
              <td>
                <i class="bi bi-eye-fill" @click="viewPatient(patient)"></i>
                <i
                  class="bi bi-pencil-fill"
                  v-if="isEditor"
                  @click="editPatient(patient)"
                ></i>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <FooterComponent />
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useAuthStore } from "../stores/auth";
import { usePatientsStore } from "../stores/patient";
import HeaderComponent from "@/components/shared/HeaderComponent.vue";
import FooterComponent from "@/components/shared/FooterComponent.vue";
import { useRouter } from "vue-router";

const authStore = useAuthStore();
const patientsStore = usePatientsStore();
const router = useRouter();

onMounted(async () => {
  try {
    await patientsStore.fetchAllPatients();
  } catch (error) {
    console.error("Error fetching patients:", error);
  }
});

const logoutAction = async () => {
  await authStore.logout();
  router.push({ name: "Home" });
};

const viewPatient = (patient) => {
  router.push({ name: "ViewPatient", params: { id: patient.id } });
};

const editPatient = (patient) => {
  router.push({ name: "EditPatient", params: { id: patient.id } });
};

const formatAddress = (address) => {
  return address
    ? `${address.street} ${address.street_number}, ${address.zip_code}`
    : "No Address";
};

// Retrieve the user object from local storage and parse json for is_editor
const userStr = localStorage.getItem('user');
const user = JSON.parse(userStr);
const isEditor = user.is_editor;
console.log(isEditor);

// Use computed property to make sure data is reactive
const patients = patientsStore.patients;
</script>

<style scoped>
.dashboard-container {
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.8);
  /* Slightly transparent background */
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  /* Soft shadow for depth */
}

.mdc-table {
  width: 100%;
  background-color: #f0f0f0;
  border-collapse: collapse;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  /* Shadow for the table */
}

.mdc-table th,
.mdc-table td {
  padding: 12px 15px;
  border: 1px solid #ddd;
  /* Light border for table cells */
}

.mdc-table th {
  background-color: #00a896;
  /* Mint color for header */
  color: white;
}

.mdc-button {
  background-color: #02c39a;
  /* Mint color for button */
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.mdc-button:hover {
  background-color: #028090;
  /* Darker shade on hover */
}

.logout-button {
  margin-bottom: 20px;
}

.table-responsive {
  overflow-x: auto;
  /* Responsive table */
}
</style>