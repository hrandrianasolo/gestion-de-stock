from django.db import models

DEFAULT_ID = 1


class Provider(models.Model):
    name = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    address = models.TextField()
    zip_code = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.name

    
class Article(models.Model):
    name = models.CharField(max_length=500, default="")
    price = models.FloatField()
    barcode = models.IntegerField()
    stock = models.IntegerField(default=0)
    seuil = models.IntegerField(default=0)
    is_sold_with_weight = models.BooleanField()
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE, default=DEFAULT_ID)

    def __str__(self):
        return self.name
