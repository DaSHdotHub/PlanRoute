from django.test import TestCase
from core.models import Patient, Address

class PatientModelTest(TestCase):
    def test_create_patient(self):
        address = Address.objects.create(street="Postplatz", street_number="1", zip_code="01067", city="Dresden", country="Germany")
        patient = Patient.objects.create(firstname="Max", lastname="Mustermann", address=address)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(patient.firstname, "Max")
