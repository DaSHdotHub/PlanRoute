from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Patient, Address
from rest_framework.authtoken.models import Token

class PatientService:
    @staticmethod
    def create_or_update_patient(patient_data, address_data):
        address, _ = Address.objects.get_or_create(**address_data)
        patient_data['address'] = address
        patient, created = Patient.objects.get_or_create(
            firstname=patient_data['firstname'],
            lastname=patient_data['lastname'],
            birth_date=patient_data['birth_date'],
            defaults=patient_data
        )
        return patient, created

class AddressService:
    @staticmethod
    def create_or_update_address(address_data):
        address, created = Address.objects.get_or_create(**address_data)
        return address, created

class UserService:
    @staticmethod
    def register_user(user_data):
        user = User.objects.create_user(**user_data)
        if 'is_editor' in user_data and user_data['is_editor']:
            crud_group = Group.objects.get(name='CRUD Users')
            user.groups.add(crud_group)
        else:
            readonly_group = Group.objects.get(name='Read-Only Users')
            user.groups.add(readonly_group)
        user.save()

        token, _ = Token.objects.get_or_create(user=user)
        UserService.send_confirmation_email(user.email, token.key)
        return user

    @staticmethod
    def send_confirmation_email(email, token_key):
        domain_url = settings.DOMAIN_URL
        confirmation_url = f'{domain_url}/confirm/{token_key}'
        html_content = render_to_string('email_confirmation.html', {'confirmation_url': confirmation_url})
        text_content = strip_tags(html_content)
        send_mail(
            subject='Confirm your Account',
            message=text_content,
            html_message=html_content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )