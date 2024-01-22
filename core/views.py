from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Patient, Address, Distance
from .serializers import PatientSerializer, AddressSerializer, DistanceSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        # Initialize the serializer with the request data and validate it.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        address_serializer = AddressSerializer(data=request.data.get('address'))
        if address_serializer.is_valid(raise_exception=True):
            address_data = address_serializer.validated_data
            address, address_created = Address.objects.get_or_create(**address_data)
            # Attempt to retrieve an existing patient or create a new one based on the unique fields.
            # The 'defaults' argument contains additional data for creating a new patient.
            # The 'address' argument is the address object created above.
            patient_data = serializer.validated_data
            patient_data['address'] = address
            patient, patient_created = Patient.objects.get_or_create(
                firstname=patient_data['firstname'],
                lastname=patient_data['lastname'],
                birth_date=patient_data.get('birth_date', None),
                defaults={
                    'address': address,
                    'gender': patient_data.get('gender', ''),
                    'creator': patient_data.get('creator'),
                    'last_editor': patient_data.get('last_editor')
                }
            )
            # Return the patient ID and a 201 status code if the patient was created.
            if patient_created:
                headers = self.get_success_headers(serializer.data)
                return Response(patient.id, status=status.HTTP_201_CREATED, headers=headers)
            # Return the patient ID and a 200 status code if the patient already exists.
            else:
                return Response({"message": "Patient already exists", "id": patient.id}, status=status.HTTP_200_OK)
        # Return a 400 status code if the address data is invalid.
        return Response(serializer.errors, status=status.HTTP_400_BAD_BAD_REQUEST)
    
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    def create(self, request, *args, **kwargs):
        # Initialize the serializer with the request data and validate it.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Attempt to retrieve an existing address or create a new one based on the unique fields.
        # The 'defaults' argument contains additional data for creating a new address.
        address, created = Address.objects.get_or_create(
            street=serializer.validated_data['street'],
            street_number=serializer.validated_data['street_number'],
            zip_code=serializer.validated_data['zip_code'],
            city=serializer.validated_data['city'],
            country=serializer.validated_data['country'],
            defaults=serializer.validated_data
        )

        # Return the address ID and a 201 status code if the address was created.
        if created:
            headers = self.get_success_headers(serializer.data)
            return Response(address.id, status=status.HTTP_201_CREATED, headers=headers)
        # Return the address ID and a 200 status code if the address already exists.
        else:
            return Response({"message": "Address already exists", "id": address.id}, status=status.HTTP_200_OK)

class DistanceViewSet(viewsets.ModelViewSet):
    queryset = Distance.objects.all()
    serializer_class = DistanceSerializer