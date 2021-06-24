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

