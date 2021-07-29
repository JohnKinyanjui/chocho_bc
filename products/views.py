from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import *


class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                "code": 0,
                "data": serializer.data
            })
        
        return JsonResponse({
            "code":1,
            "errors":serializer.errors
        })
    def get(self, request):
        products = ProductModel.objects.all().values()
        return JsonResponse({
            "code": 0,
            "data": list(products)
        })

