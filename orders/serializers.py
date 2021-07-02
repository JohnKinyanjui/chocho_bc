from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    account = serializers.CharField(max_length=250)

    class Meta:
        model = OrderModel
        fields = ['account']
        read_only_fields = ['orderId', 'paid', 'totalCost', 'delivered']

    def validate_account(self, account: str):
        try:
            account = AccountModel.objects.get(token=account)
            return account
        except Exception as e:
            return serializers.ValidationError("Authorization Failed")


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.CharField(max_length=250)
    product = serializers.CharField(max_length=250)

    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'clientName']

    def validate_order(self, order: str):
        try:
            order = OrderModel.objects.get(order_id=order)
            return order
        except Exception as e:
            return serializers.ValidationError("This Order does not exists")

    def validate_product(self, product: str):
        try:
            p = ProductModel.objects.get(product_id=product)
            return p
        except Exception as e:
            return serializers.ValidationError("This product not found")
