from django.contrib import admin
from .models import Patient, Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'street_number', 'city', 'country')
    search_fields = ('street', 'city', 'country')
    
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'birth_date', 'address', 'created_at', 'creator', 'last_editor')
    search_fields = ('lastname', 'firstname')
    list_filter = ('birth_date', 'created_at')