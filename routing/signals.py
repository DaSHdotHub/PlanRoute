from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Address
from .utils import create_and_calculate_address_pairs, update_coordinates

@receiver(post_save, sender=Address)
def update_lat_long(sender, instance, created, **kwargs):
    if created or instance.latitude is None or instance.longitude is None:
        # Call function to update latitude and longitude
        update_coordinates(instance)
        
@receiver(post_save, sender=Address)
def address_updated(sender, instance, **kwargs):
    create_and_calculate_address_pairs()
