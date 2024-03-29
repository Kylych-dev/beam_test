from django.db import models
from apps.accounts.models import CustomUser

class Store(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    locations = models.CharField(max_length=255, verbose_name="Locations")
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='establishments')

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __str__(self):
        return self.name