from rest_framework import serializers
from .models import Patient, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Patient
        fields = ['id', 'gender', 'firstname', 'lastname', 'birth_date', 'address', 'creator', 'last_editor']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        patient = Patient.objects.create(address=address, **validated_data)
        return patient