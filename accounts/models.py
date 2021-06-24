import uuid

from django.db import models

from products.models import ProductModel


class AccountModel(models.Model):
    profileImage = models.ImageField(upload_to="chocho/images")
    fullName = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=50)
    token = models.CharField(max_length=250, null=True)


class AccountOtp(models.Model):
    phoneNumber = models.CharField(max_length=50)
    otp = models.IntegerField()


class AccountGroup(models.Model):
    groupId = models.UUIDField(default=uuid.uuid4, editable=False)
    account = models.ForeignKey(AccountModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    details = models.CharField(max_length=250)


class AccountGroupItem(models.Model):
    group = models.ForeignKey(AccountGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    details = models.CharField(max_length=250)
    product = models.ForeignKey(ProductModel, null=True, on_delete=models.CASCADE)
