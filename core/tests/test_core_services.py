from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.models import User
from core.services import PatientService
from core.models import Patient, Address

class PatientServiceTestCase(TestCase):

    def setUp(self):
        self.address_data = {"street": "Postplatz", "street_number": "1",
                             "zip_code": "01067", "city": "Dresden", "country": "Germany"}
        self.patient_data = {
            "firstname": "Max",
            "lastname": "Mustermann",
            "birth_date": timezone.now().date()
        }

    def create_address(self, **kwargs):
        return Address.objects.create(**self.address_data, **kwargs)

    def test_create_new_patient(self):
        """Test creating a new patient with unique forename, lastname, and birthday."""
        patient, created = PatientService.create_or_update_patient(
            self.patient_data, self.address_data)
        self.assertTrue(created, "Expected patient to be created.")
        self.assertEqual(Patient.objects.count(), 1,
                         "Expected one patient in the database.")
        self.assertEqual(patient.firstname, "Max")
        self.assertEqual(patient.lastname, "Mustermann")
        self.assertEqual(patient.birth_date, self.patient_data["birth_date"])

    def test_update_patient_by_id_birth_date(self):
        original_patient, _ = PatientService.create_or_update_patient(
            self.patient_data, self.address_data)
        original_id = original_patient.id
        new_birth_date = self.patient_data["birth_date"] - timezone.timedelta(days=365)

        # Simulating an update operation
        Patient.objects.filter(id=original_id).update(birth_date=new_birth_date)
        
        updated_patient = Patient.objects.get(id=original_id)
        self.assertEqual(updated_patient.birth_date, new_birth_date, "The patient's birth date should be updated.")
        self.assertEqual(updated_patient.id, original_id, "The patient's ID should remain constant.")
        
    def test_update_patient_gender_and_last_editor(self):
        original_patient, _ = PatientService.create_or_update_patient(self.patient_data, self.address_data)
        original_id = original_patient.id
        
        # Create a new editor user
        new_last_editor = User.objects.create_user(username='neweditor', password='testpassword')
        
        new_gender = 'U'  # Assuming original was not 'U'
        
        # Update operation
        Patient.objects.filter(id=original_id).update(gender=new_gender, last_editor=new_last_editor)
        
        updated_patient = Patient.objects.get(id=original_id)
        self.assertEqual(updated_patient.gender, new_gender, "The patient's gender should be updated.")
        self.assertEqual(updated_patient.last_editor, new_last_editor, "The patient's last editor should be updated.")
        self.assertEqual(updated_patient.id, original_id, "The patient's ID should remain constant.")

    def test_create_patient_with_same_name_different_birthday(self):
        """Test that a new patient with the same name but a different birthday is treated as a unique entry."""
        PatientService.create_or_update_patient(
            self.patient_data, self.address_data)
        new_patient_data = self.patient_data.copy()
        new_patient_data["birth_date"] = self.patient_data["birth_date"] - \
            timezone.timedelta(days=3650)  # 10 years earlier
        patient, created = PatientService.create_or_update_patient(
            new_patient_data, self.address_data)
        self.assertTrue(created, "Expected a new patient to be created.")
        self.assertEqual(Patient.objects.count(), 2,
                         "Expected two unique patients in the database.")
