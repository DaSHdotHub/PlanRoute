from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from django.shortcuts import render
import os

from core.models import Patient, Address, Distance
from core.serializers import (
    PatientSerializer,
    AddressSerializer,
    DistanceSerializer,
    UserSerializer,
)
from core.services import PatientService, UserService, AddressService


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
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(is_active=False)
            user.set_password(request.data["password"])
            user.save()

            # Directly assign user to group based on 'is_editor' field
            group_name = (
                "CRUD Users"
                if request.data.get("is_editor", False)
                else "Read-Only Users"
            )
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            user.save()

            # Generate token for email confirmation
            token, created = Token.objects.get_or_create(user=user)
            # Determine the base domain based on the environment
            if os.environ.get("DEVELOPMENT", "False") == "True":
                domain_url = "http://localhost:8000"
            elif os.environ.get("DEVELOPMENT_URL", "") != "":
                domain_url = os.environ.get("DEVELOPMENT_URL")
            else:
                domain_url = os.environ.get("PRODUCTION_URL")

            url_key = "/redirect/"

            # Prepare email content
            confirmation_url = f"{domain_url}{url_key}{token.key}"
            html_content = render_to_string(
                "email_confirmation.html", {"confirmation_url": confirmation_url}
            )
            # Plain text version for email clients that don't support HTML
            text_content = strip_tags(html_content)
            # Send confirmation email
            send_mail(
                subject="Confirm your PlanRoute Account",
                message=text_content,
                html_message=html_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Confirm user account
    @action(methods=["GET"], detail=False, url_path="confirm/(?P<key>.+)")
    def confirm(self, request, key=None):
        try:
            token = Token.objects.get(key=key)
            user = token.user
            if not user.is_active:
                user.is_active = True
                user.save()
                token.delete()
                return Response(
                    {"message": "Account successfully activated"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"message": "Account already active"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Token.DoesNotExist:
            return Response(
                {"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )
