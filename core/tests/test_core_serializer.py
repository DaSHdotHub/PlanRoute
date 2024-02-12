from rest_framework.test import APITestCase
from core.serializers import PatientSerializer

class PatientSerializerTest(APITestCase):
    def test_valid_serializer(self):
        valid_serializer_data = {
            "firstname": "Max",
            "lastname": "Mustermann",
            "address": {
                "street": "Postplatz",
                "street_number": "1",
                "zip_code": "01067",
                "city": "Dresden",
                "country": "Germany"
            }
        }
        serializer = PatientSerializer(data=valid_serializer_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        invalid_serializer_data = {}  # Assuming this is missing required fields
        serializer = PatientSerializer(data=invalid_serializer_data)
        self.assertFalse(serializer.is_valid())
