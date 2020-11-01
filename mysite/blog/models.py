from django.conf import settings
from django.db import models
from django.utils import timezone
DEFAULT_ID = 1

class Provider(models.Model):
    name = models.CharField(max_length = 500, default= "")
    phoneNumber = models.FloatField()
    address = models.CharField(max_length = 500, default= "")
    zipCode = models.FloatField()

class Article(models.Model):
    name = models.CharField(max_length = 500, default= "")
    price = models.FloatField()
    barcode = models.FloatField()
    inStock = models.IntegerField(default=0)
    seuil = models.IntegerField(default=0)
    isSaleInWeight = models.BooleanField()
    id_provider = models.ForeignKey('Provider',on_delete=models.CASCADE, default=DEFAULT_ID)

