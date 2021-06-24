from .models import *
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ['profileImage', 'fullName', 'phoneNumber']


class AccountOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountOtp
        fields = ['phoneNumber', 'otp']


class AccountGroupSerializer(serializers.ModelSerializer):
    account = serializers.CharField(max_length=250)

    class Meta:
        model = AccountGroup
        fields = ['account', 'name', 'details']

    def validate_account(self, account):
        try:
            a = AccountModel.objects.get(token=account)
            return a
        except Exception as e:
            return serializers.ValidationError("This Account does not exists")


class AccountGroupItemSerializer(serializers.ModelSerializer):
    group = serializers.CharField(max_length=250)
    product = serializers.CharField(max_length=250)

    class Meta:
        model = AccountGroupItem
        fields = ['group', 'name', 'details', 'product']

    def validate_group(self, group: str):
        try:
            group = AccountGroupItem.objects.get(group__name=group)
            return group
        except Exception as e:
            return serializers.ValidationError("This Account does not exists")

    def validate_product(self, product :str):
        try:
            product = ProductModel.objects.get(product_id=product)
            return product
        except Exception as e:
            return serializers.ValidationError("This Product does not exists")
