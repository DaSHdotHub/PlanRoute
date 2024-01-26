from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
import os

from .models import Patient, Address, Distance
from .serializers import PatientSerializer, AddressSerializer, DistanceSerializer, UserSerializer


class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        # Initialize the serializer with the request data and validate it.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        address_serializer = AddressSerializer(
            data=request.data.get('address'))
        if address_serializer.is_valid(raise_exception=True):
            address_data = address_serializer.validated_data
            address, address_created = Address.objects.get_or_create(
                **address_data)
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
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    queryset = Distance.objects.all()
    serializer_class = DistanceSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Register a new user
    @action(methods=['POST'], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(is_active=False)
            
            # Hash the password
            if 'password' in request.data:
                user.set_password(request.data['password'])
                user.save()
            # Assign user to group based on the 'is_editor' field
            if 'is_editor' in request.data and request.data['is_editor']:
                crud_group = Group.objects.get(name='CRUD Users')
                user.groups.add(crud_group)
            else:
                readonly_group = Group.objects.get(name='Read-Only Users')
                user.groups.add(readonly_group)

            user.save()
            
            token, created = Token.objects.get_or_create(user=user)

            # Determine the base domain based on the environment
            is_development = os.environ.get('DEVELOPMENT', 'False') == 'True'
            domain_url = 'http://localhost:8000' if is_development else os.environ.get('PRODUCTION_DOMAIN', 'https://your_production_domain.com')

            # confirmation endpoint
            url_key = '/redirect/'

            # Prepare email content
            confirmation_url = f'{domain_url}{url_key}{token.key}'
            html_content = render_to_string('email_confirmation.html', {
                                            'confirmation_url': confirmation_url})
            # Plain text version for email clients that don't support HTML
            text_content = strip_tags(html_content)
            # Send confirmation email
            send_mail(
                subject='Confirm your PlanRoute Account',
                message=text_content,
                html_message=html_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False, url_path='confirm/(?P<key>.+)')
    def confirm(self, request, key=None):
        try:
            token = Token.objects.get(key=key)
            user = token.user
            if not user.is_active:
                user.is_active = True
                user.save()
                token.delete()
                return Response({"message": "Account successfully activated"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Account already active"}, status=status.HTTP_400_BAD_REQUEST)
        except Token.DoesNotExist:
            return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

