from django.http import JsonResponse
from rest_framework.views import APIView

from helpers.payments.utils import mpesa_paybill
from orders.serializers import *
from accounts.models import *


# gets the group that wants to create order
# creates an order model
# gets the group item
# creates order items from the group item
# pay for the order after its creates
# expiration of an order is one day

class OrderView(APIView):
    def post(self, request):
        data = request.data
        try:
            serializer = OrderSerializer(data={"account": data["account"]})
            if serializer.is_valid():
                serializer.save()
                items = AccountGroupItem.objects.filter(group__account__token=data['token'],
                                                        group__groupId=data['groupId']).all().values()
                order = OrderModel.objects.get(order_id=serializer.data['orderId'])
                for item in items:
                    orderItem = OrderItem(
                        order=order,
                        product=item.product,
                        name=item.name
                    )
                    orderItem.save()

                return JsonResponse({
                    "code": 0,
                    "message": "New Order Created"
                })

            return JsonResponse({
                "code": 1,
                "errors": serializer.errors
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                "code": 1,
                "errors": "Something went wrong"
            })

    def get(self, request):
        try:
            orders = OrderModel.objects.filter(account__token=request.GET['token']).values()
            return JsonResponse({
                "code": 0,
                "data": list(orders)
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                "code": 1,
                "errors": "Something went wrong"
            })


class OrderItemView(APIView):
    def post(self, request):
        try:
            serializer = OrderItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({
                    "code": 0,
                    "message": "New Order Item Created"
                })

            return JsonResponse({
                "code": 1,
                "errors": serializer.errors
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                "code": 1,
                "errors": "Something went wrong"
            })

    def get(self, request):
        orderItems = OrderItem.objects.get(order__order_id=request.GET['orderId'])
        return JsonResponse({
            "code": 0,
            "data": list(orderItems)
        })


class PaymentView(APIView):
    def post(self, request):
        data = request.data
        try:
            r = mpesa_paybill(data['PhoneNumber'], ['Amount'])
            if ['code'] == 0:
                OrderModel.objects.filter(orderId=data['orderId']).update(paid=True)
                return JsonResponse({
                    "code":0,
                    "message":"order updates"
                })

            return JsonResponse({
                "code": 1,
                "message": "Something went wrong"
            })
        except Exception as e:
            return JsonResponse({
                "code": 1,
                "message": "Something went wrong"
            })

    def get(self, request):
        pass
