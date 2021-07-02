from .models import *
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ['profileImage', 'fullName', 'phoneNumber', 'token']
    
    def validate_phoneNumber(self, phoneNumber :str):
        otpExists = AccountOtp.objects.filter(phoneNumber=phoneNumber).exists()
        if(otpExists):
            return phoneNumber
        
        raise serializers.ValidationError("Phone Number not verified")  


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
            raise serializers.ValidationError("This Account does not exists")


class AccountGroupItemSerializer(serializers.ModelSerializer):
    group = serializers.CharField(max_length=250)
    product = serializers.CharField(max_length=250)

    class Meta:
        model = AccountGroupItem
        fields = ['group', 'name', 'phoneNumber', 'details', 'product']

    def validate_group(self, group: str):
        try:
            group = AccountGroup.objects.get(groupId=group)
            return group
        except Exception as e:
            raise serializers.ValidationError(str(e))

    def validate_product(self, product :str):
        try:
            product = ProductModel.objects.get(productId=product)
            return product
        except Exception as e:
            raise serializers.ValidationError("This Product does not exists")
