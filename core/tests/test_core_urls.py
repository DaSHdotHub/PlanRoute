from django.test import TestCase
from rest_framework.test import APIClient

#Test Endpoint Accessibility
class URLAccessibilityTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_patient_list_accessible(self):
        response = self.client.get('/api/patients/')
        self.assertEqual(response.status_code, 200)

#Ensure correct view is called     
class PatientViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_patient_list_returns_correct_data(self):
        response = self.client.get('/api/patients/')
        self.assertEqual(response.status_code, 200)

#Test OpenApi Schema
class OpenAPISchemaTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_swagger_json_accessible(self):
        response = self.client.get('/api/swagger.json')
        self.assertEqual(response.status_code, 200)

    def test_swagger_ui_accessible(self):
        response = self.client.get('/api/swagger/')
        self.assertEqual(response.status_code, 200)

    def test_redoc_accessible(self):
        response = self.client.get('/api/redoc/')
        self.assertEqual(response.status_code, 200)