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
        # Check if an address with these details already exists
        address, created = Address.objects.get_or_create(
            street=address_data['street'],
            street_number=address_data['street_number'],
            zip_code=address_data['zip_code'],
            city=address_data['city'],
            country=address_data['country'],
            defaults=address_data
        )
        # Create the patient with the existing or new address
        patient = Patient.objects.create(address=address, **validated_data)
        return patient