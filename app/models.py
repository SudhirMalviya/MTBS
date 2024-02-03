from django.db import models
from cities_light.models import Country, City
# Create your models here.
class Address(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.country}, {self.city}"