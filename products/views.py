from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import *


class ProductView(APIView):
    def get(self, request):
        products = ProductModel.objects.all().values()
        return JsonResponse({
            "code": 0,
            "data": list(products)
        })


class OrderView(APIView):
    def post(self, request):
        try:
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
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
                "code":0,
                "data":list(orders)
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                "code":1,
                "errors":"Something went wrong"
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
        orderItems = OrderItem.objects.get(order__order_id= request.GET['orderId'])
        return JsonResponse({
            "code":0,
            "data": list(orderItems)
        })


