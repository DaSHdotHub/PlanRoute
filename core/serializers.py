from rest_framework import serializers, status
from rest_framework.response import Response
from .models import Patient, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        address, created = Address.objects.get_or_create(
            street=validated_data['street'],
            street_number=validated_data['street_number'],
            zip_code=validated_data['zip_code'],
            city=validated_data['city'],
            country=validated_data['country'],
            defaults=validated_data
        )
        if created:
            return Response({'message': 'New address created.', 'address': address}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Address already exists.', 'address': address}, status=status.HTTP_200_OK)


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