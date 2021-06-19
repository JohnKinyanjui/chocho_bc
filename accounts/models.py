from django.db import models


class AccountModel(models.Model):
    profileImage = models.ImageField(upload_to="chocho/images")
    fullName = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=50)
    token = models.CharField(max_length=250, null=True)


class AccountOtp(models.Model):
    phoneNumber = models.CharField(max_length=50)
    otp = models.IntegerField()


class AccountGroup(models.Model):
    account = models.ForeignKey(AccountModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
