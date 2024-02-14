from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.shortcuts import render
from django.core.exceptions import ValidationError
from core.models import Patient, Address, Distance
from core.serializers import (
    PatientSerializer,
    AddressSerializer,
    DistanceSerializer,
    UserSerializer,
)
from core.services import PatientService, UserService


def landing_page(request):
    return render(request, "landing_page.html")


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient_data = serializer.validated_data

        address_serializer = AddressSerializer(data=request.data.get("address"))
        if address_serializer.is_valid(raise_exception=True):
            address_data = address_serializer.validated_data

            patient, created = PatientService.create_or_update_patient(
                patient_data, address_data
            )

            if created:
                headers = self.get_success_headers(serializer.data)
                return Response(
                    patient.id, status=status.HTTP_201_CREATED, headers=headers
                )
            else:
                return Response(
                    {"message": "Patient already exists", "id": patient.id},
                    status=status.HTTP_200_OK,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        # Initialize the serializer with the request data and validate it.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Attempt to retrieve an existing address or create a new one based on the unique fields.
        # The 'defaults' argument contains additional data for creating a new address.
        address, created = Address.objects.get_or_create(
            street=serializer.validated_data["street"],
            street_number=serializer.validated_data["street_number"],
            zip_code=serializer.validated_data["zip_code"],
            city=serializer.validated_data["city"],
            country=serializer.validated_data["country"],
            defaults=serializer.validated_data,
        )

        # Return the address ID and a 201 status code if the address was created.
        if created:
            headers = self.get_success_headers(serializer.data)
            return Response(address.id, status=status.HTTP_201_CREATED, headers=headers)
        # Return the address ID and a 200 status code if the address already exists.
        else:
            return Response(
                {"message": "Address already exists", "id": address.id},
                status=status.HTTP_200_OK,
            )


class DistanceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    queryset = Distance.objects.all()
    serializer_class = DistanceSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["POST"], detail=False)
    def register(self, request):
        try:
            user = UserService.register_user(request.data)
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(e.message_dict, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["GET"], detail=False, url_path="confirm/(?P<key>.+)")
    def confirm(self, request, key=None):
        message, success = UserService.confirm_user(key)
        if success:
            return Response({"message": message}, status=status.HTTP_200_OK)
        else:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
