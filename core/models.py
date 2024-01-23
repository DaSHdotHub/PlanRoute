from django.conf import settings
from django.db import models

# Create your models here.
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
    
class Distance(models.Model):
    from_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="distance_from")
    to_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="distance_to")
    distance_in_km = models.FloatField(null=True, blank=True, help_text="Distance in kilometers")
    last_updated = models.DateTimeField(null=True, blank=True, auto_now=True)
    travel_mode = models.CharField(max_length=10, default='car', help_text="Mode of travel")
    depart_at = models.DateTimeField(null=True, blank=True, help_text="Departure time")


    def __str__(self):
        return f"{self.distance_in_km} km from {self.from_address} to {self.to_address}"

    
class Patient(models.Model):
    """Model representing a patient."""
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('U', 'Prefer not to say')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
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