from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class PatientViewSetTest(APITestCase):
    def test_create_patient(self):
        url = reverse('patient-list')  # Assuming there is a 'patient-list' route in urls.py
        data = {
            "firstname": "Dieter",
            "lastname": "Musterhausen",
            "birth_date": "1990-01-01",
            "address": {
                "street": "Friedenstr.",
                "street_number": "23",
                "zip_code": "01097",
                "city": "Dresden",
                "country": "Germany"
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)