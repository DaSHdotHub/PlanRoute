from django.conf import settings
from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


class Address(models.Model):
    street = models.CharField(max_length=200)
    street_number = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.street} {self.street_number}, {self.city}, {self.country}"

    def update_geolocation(self):
        """
        A method to update the latitude and longitude fields
        by making an API call to e.g. TOMTOM/ GOOGLE for this address.
        """
        # API call to TOMTOM/ GOOGLE to get geolocation
        # Update self.latitude and self.longitude
        pass
    
class Distance(models.Model):
    from_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="distance_from")
    to_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="distance_to")
    distance_in_km = models.FloatField(help_text="Distance in kilometers")

    def __str__(self):
        return f"{self.distance_in_km} km from {self.from_address} to {self.to_address}"

    def update_distance(self):
        """
        A method to update the distance field by making an API call to TOMTOM/ GOOGLE.
        The method should check if the distance already exists to minimize API calls.
        """
        # API call to TOMTOM/ GOOGLE to get distance
        # Update self.distance_in_km
        pass

    
class Patient(models.Model):
    """Model representing a patient."""
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    # Link to the user who created the patient
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='created_patients',
        null=True,
        blank=True
    )
    # Link to the user who last edited the patient
    last_editor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='edited_patients',
        null=True,
        blank=True
    )

    # Represent the patient as a string on the admin page
    def __str__(self):
        return f"{self.lastname}, {self.firstname}"

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this patient."""
        return reverse('patient-detail', args=[str(self.id)])