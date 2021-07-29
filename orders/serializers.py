import uuid
from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    account = serializers.CharField(max_length=250)

    class Meta:
        model = OrderModel
        fields = ['orderId', 'account', 'delivery_time', 'delivery_date']
        read_only_fields = ['orderId', 'paid', 'totalCost', 'delivered']
    
    def validate_orderId(self, orderId: str):
        return uuid.uuid4()    

    def validate_account(self, account: str):
        print(account)
        accountExists = AccountModel.objects.filter(token=account).exists()
        if(accountExists):
            ac = AccountModel.objects.get(token=account)
            return ac
        else:
            return serializers.ValidationError("Account does not exists")


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
