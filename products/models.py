import uuid

from django.db import models

# from accounts.models import AccountModel


class ProductModel(models.Model):
    productId = models.UUIDField(default=uuid.uuid4(), unique=True)
    image = models.ImageField(upload_to="chocho/productImages", max_length=250)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    cost = models.CharField(max_length=10)

