from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vehicle, VehicleProfile


@receiver(post_save, sender=Vehicle)
def create_profile(sender, instance, created, **kwargs):
    if created:
        VehicleProfile.objects.create(context=instance)
