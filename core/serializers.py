from rest_framework import serializers
from .models import Patient, Address, Distance

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'street_number', 'zip_code', 'city', 'country', 'latitude', 'longitude']

class PatientSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Patient
        fields = ['id', 'gender', 'firstname', 'lastname', 'birth_date', 'address', 'creator', 'last_editor']
        
class DistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distance
        fields = '__all__'