from django.conf import settings
from django.db import models
from django.utils import timezone
DEFAULT_ID = 1


class Article(models.Model):
    name = models.CharField(max_length = 500, default= "")
    price = models.FloatField()
    barcode = models.IntegerField(default=0)
    inStock = models.IntegerField(default=0)
    seuil = models.IntegerField(default=0)
    isSaleInWeight = models.BooleanField()

class Provider(models.Model):
    name = models.CharField(max_length = 500, default= "")
    phoneNumber = models.IntegerField()
    address = models.CharField(max_length = 500, default= "")
    zipCode = models.IntegerField(default=0)
    id_article = models.ForeignKey('Article' ,on_delete=models.CASCADE, default=DEFAULT_ID)

class Role(models.Model):
    role = models.CharField(max_length = 500, default= "")

class User(models.Model):
    name = models.CharField(max_length = 500, default= "")
    id_role = models.ForeignKey('Role' ,on_delete=models.CASCADE, default=DEFAULT_ID)