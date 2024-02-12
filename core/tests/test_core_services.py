from django.test import TestCase
from core.services import PatientService
from core.models import Patient, Address

class PatientServiceTest(TestCase):
    def test_create_or_update_patient(self):
        address_data = {"street": "Postplatz", "street_number": "1", "zip_code": "01067", "city": "Dresden", "country": "Germany"}
        patient_data = {"firstname": "Max", "lastname": "Mustermann", "address": address_data}
        patient, created = PatientService.create_or_update_patient(patient_data, address_data)
        self.assertTrue(created)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(patient.firstname, "Max")