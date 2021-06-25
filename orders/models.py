import uuid

from django.db import models

from accounts.models import AccountModel
from products.models import ProductModel


class OrderModel(models.Model):
    orderId = models.UUIDField(default=uuid.uuid4(), unique=True, auto_created=True)
    account = models.ForeignKey(AccountModel, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
    totalCost = models.FloatField(default=0)
    delivered = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)


class OrderItem(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
