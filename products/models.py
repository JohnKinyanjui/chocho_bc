import uuid

from django.db import models

from accounts.models import AccountModel


class ProductModel(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4(), primary_key=True, unique=True, auto_created=True)
    productImage = models.ImageField(upload_to="chocho/productImages", max_length=250)
    productName = models.CharField(max_length=200)
    productDes = models.CharField(max_length=250)
    productCost = models.CharField(max_length=10)


class OrderModel(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4(), unique=True, auto_created=True)
    orderName = models.CharField(max_length=250)
    account = models.ForeignKey(AccountModel, on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    clientName = models.CharField(max_length=250)


class OrderReceipt(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
    totalCost = models.FloatField()
    delivered = models.BooleanField(default=False)

