<template>
  <div>
    <HeaderComponent />
    <div class="dashboard-container">
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
            <tr v-for="(patient, index) in paginatedPatients" :key="index">
              <td>{{ patient.id }}</td>
              <td>{{ patient.firstname }} {{ patient.lastname }}</td>
              <td>{{ formatAddress(patient.address) }}</td>
              <td>
                <button
                  class="btn btn-outline-primary btn-icon"
                  v-if="isEditor"
                  @click="editPatient(patient)"
                >
                  <i class="bi bi-pencil-fill"></i>
                </button>
                <button
                  class="btn btn-outline-primary btn-icon"
                  v-else
                  @click="viewPatient(patient)"
                >
                  <i class="bi bi-eye-fill"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- Pagination controls -->
      <div class="pagination-controls">
        <!-- Dropdown to select number of entries per page -->
        <select v-model="entriesPerPage">
          <option v-for="option in entriesPerPageOptions" :key="option">
            {{ option }}
          </option>
        </select>
        <!-- Previous and next page buttons -->
        <button @click="prevPage">Previous</button>
        <button @click="nextPage">Next</button>
      </div>
    </div>
    <FooterComponent />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { usePatientsStore } from "../stores/patient";
import HeaderComponent from "@/components/shared/HeaderComponent.vue";
import FooterComponent from "@/components/shared/FooterComponent.vue";
import { useRouter } from "vue-router";

const patientsStore = usePatientsStore();
const router = useRouter();

// Data properties
const patients = ref([]);
const currentPage = ref(1);
const entriesPerPage = ref(10); // Default value
const entriesPerPageOptions = [10, 20, 50, 100];

// Fetch patients on component mount
onMounted(async () => {
  await patientsStore.fetchAllPatients();
  patients.value = patientsStore.patients;
});

// Computed property for paginated data
const paginatedPatients = computed(() => {
  const startIndex = (currentPage.value - 1) * entriesPerPage.value;
  const endIndex = startIndex + entriesPerPage.value;
  return patients.value.slice(startIndex, endIndex);
});

// Methods for pagination
const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

const nextPage = () => {
  const totalPages = Math.ceil(patients.value.length / entriesPerPage.value);
  if (currentPage.value < totalPages) {
    currentPage.value++;
  }
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
const isEditor = user?.is_editor; 

</script>

<style scoped>
/* Pagination controls styling */
.pagination-controls {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}


/* Slightly transparent background */
.dashboard-container {
  padding: 20px 20px 200px;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

/* Shadow for the table */
.mdc-table {
  width: 100%;
  background-color: #f0f0f0;
  border-collapse: collapse;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Light border for table cells */
.mdc-table th,
.mdc-table td {
  padding: 12px 15px;
  border: 1px solid #ddd;
}

/* Mint color for header */
.mdc-table th {
  background-color: #00a896;
  color: white;
}

/* Responsive table */
.table-responsive {
  overflow-x: auto;
}
/* Custom button styles */
.btn {
  color: #007770; /* White color on hover */
  border-color: #007770;
}
.btn:hover {
  background-color: #f0f0f0;
  border-color: black;
}
.btn-icon {
  border-radius: 8px; /* Rectangle shape */
  padding: 8px;
}
</style>
