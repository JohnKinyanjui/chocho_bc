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
        model = AccountModel
        fields = ['account', 'name']

    def validate_account(self, account):
        try:
            a = AccountModel.objects.get(token=account)
            return a
        except Exception as e:
            return serializers.ValidationError("This Account does not exists")
