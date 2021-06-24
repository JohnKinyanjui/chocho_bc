import uuid

from django.db import models

# from accounts.models import AccountModel


class ProductModel(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4(), primary_key=True, unique=True, auto_created=True)
    productImage = models.ImageField(upload_to="chocho/productImages", max_length=250)
    productName = models.CharField(max_length=200)
    productDes = models.CharField(max_length=250)
    productCost = models.CharField(max_length=10)

