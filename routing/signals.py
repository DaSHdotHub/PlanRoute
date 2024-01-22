from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Address
from .utils import update_coordinates, create_address_pairs, identify_missing_distances

@receiver(post_save, sender=Address)
def address_post_save(sender, instance, created, **kwargs):
    if created or instance.latitude is None or instance.longitude is None:
        update_coordinates(instance)

    # Check if there are at least two addresses
    if Address.objects.count() > 1:
        create_address_pairs()

    # Optionally, identify missing distances
    identify_missing_distances()
