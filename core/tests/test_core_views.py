from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail


class PatientViewSetTest(APITestCase):
    def test_create_patient(self):
        url = reverse(
            "patient-list"
        )  # Assuming there is a 'patient-list' route in urls.py
        data = {
            "firstname": "Dieter",
            "lastname": "Musterhausen",
            "birth_date": "1990-01-01",
            "address": {
                "street": "Friedenstr.",
                "street_number": "23",
                "zip_code": "01097",
                "city": "Dresden",
                "country": "Germany",
            },
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# UserRegistration Integration Test
class UserRegistrationTestCase(APITestCase):
    def test_user_registration(self):
        url = "/api/users/register/"

        # Define the data for creating a new user
        user_data = {
            "username": "testuser",
            "password": "testpassword123",
            "email": "testuser@example.com",
            "is_editor": True,  # or False
        }

        # Send a POST request to the register endpoint
        response = self.client.post(url, user_data, format="json")

        # Check that the response indicates successful creation
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the user is created in the database
        user_exists = User.objects.filter(username=user_data["username"]).exists()
        self.assertTrue(user_exists)

        # Confirm the user is inactive awaiting email confirmation
        user = User.objects.get(username=user_data["username"])
        self.assertFalse(user.is_active)

        # Check that an email has been sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn(user.email, mail.outbox[0].to)

    def test_user_registration_duplicate_username(self):
        url = "/api/users/register/"

        # Define the data for creating a new user
        user_data = {
            "username": "testuserduplicate",
            "password": "testpassword123",
            "email": "testuserduplicate@example.com",
            "is_editor": False,
        }

        # Send the first POST request to the register endpoint
        response_first = self.client.post(url, user_data, format="json")
        # Check that the response indicates successful creation
        self.assertEqual(response_first.status_code, status.HTTP_201_CREATED)

        # Attempt to register the same user again
        response_second = self.client.post(url, user_data, format="json")
        # This time, the request should fail with a 400 Bad Request status
        self.assertEqual(response_second.status_code, status.HTTP_400_BAD_REQUEST)

        # Verify the response includes an error message about the username
        self.assertContains(
            response_second, "username", status_code=status.HTTP_400_BAD_REQUEST
        )

        # Verify the number of users in the database to ensure only one user was created.
        self.assertEqual(User.objects.filter(username=user_data["username"]).count(), 1)
