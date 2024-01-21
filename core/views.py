from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Patient, Address
from .serializers import PatientSerializer, AddressSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        address_serializer = AddressSerializer(data=request.data.get('address'))
        if address_serializer.is_valid(raise_exception=True):
            address_data = address_serializer.validated_data
            address, address_created = Address.objects.get_or_create(**address_data)

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

            if patient_created:
                headers = self.get_success_headers(serializer.data)
                return Response(patient.id, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response({"message": "Patient already exists", "id": patient.id}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_BAD_REQUEST)
    
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        address, created = Address.objects.get_or_create(
            street=serializer.validated_data['street'],
            street_number=serializer.validated_data['street_number'],
            zip_code=serializer.validated_data['zip_code'],
            city=serializer.validated_data['city'],
            country=serializer.validated_data['country'],
            defaults=serializer.validated_data
        )

        if created:
            headers = self.get_success_headers(serializer.data)
            return Response(address.id, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"message": "Address already exists", "id": address.id}, status=status.HTTP_200_OK)