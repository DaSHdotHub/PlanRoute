from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
import os
from django.conf import settings

from core.models import Address, Patient


class PatientService:
    @staticmethod
    def create_or_update_patient(patient_data, address_data):
        address, _ = Address.objects.get_or_create(**address_data)
        patient_data["address"] = address
        patient, created = Patient.objects.get_or_create(
            firstname=patient_data["firstname"],
            lastname=patient_data["lastname"],
            birth_date=patient_data["birth_date"],
            defaults=patient_data,
        )
        return patient, created


class AddressService:
    @staticmethod
    def create_or_update_address(address_data):
        address, created = Address.objects.get_or_create(**address_data)
        return address, created


class UserService:
    @staticmethod
    def register_user(data):
        """
        Handles the registration of a new user.
        """
        # Check for duplicate username
        if User.objects.filter(username=data["username"]).exists():
            raise ValidationError(
                {"username": ["A user with that username already exists."]}
            )

        user = User.objects.create_user(
            username=data["username"],
            email=data["email"],
            password=data["password"],
            is_active=False,  # User will be activated after email confirmation
        )

        # Assign user to group based on 'is_editor' field
        group_name = "CRUD Users" if data.get("is_editor", False) else "Read-Only Users"
        group = Group.objects.get(name=group_name)
        user.groups.add(group)

        # Generate token for email confirmation
        token, _ = Token.objects.get_or_create(user=user)

        # Determine the base domain based on the environment
        domain_url = UserService._get_domain_url()

        confirmation_url = f"{domain_url}/redirect/{token.key}"

        # Prepare and send email
        UserService._send_confirmation_email(user.email, confirmation_url)

        return user

    @staticmethod
    def _get_domain_url():
        if os.environ.get("DEVELOPMENT", "False") == "True":
            return "http://localhost:8080"
        elif os.environ.get("DEVELOPMENT_URL", "") != "":
            return os.environ.get("DEVELOPMENT_URL")
        return os.environ.get("PRODUCTION_URL")

    @staticmethod
    def _send_confirmation_email(email, confirmation_url):
        html_content = render_to_string(
            "email_confirmation.html", {"confirmation_url": confirmation_url}
        )
        text_content = strip_tags(html_content)
        send_mail(
            subject="Confirm your PlanRoute Account",
            message=text_content,
            html_message=html_content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )

    @staticmethod
    def confirm_user(key):
        """
        Confirms a user's email and activates their account.
        """
        try:
            token = Token.objects.get(key=key)
            user = token.user
            if not user.is_active:
                user.is_active = True
                user.save()
                token.delete()
                return {"message": "Account successfully activated"}, True
            else:
                return {"message": "Account already active"}, False
        except Token.DoesNotExist:
            return {"message": "Invalid token"}, False

    @staticmethod
    def login_user(data):
        """
        Handles the login of a user.
        """
        user = User.objects.filter(username=data["username"]).first()
        if user and user.check_password(data["password"]):
            return user
        return None
