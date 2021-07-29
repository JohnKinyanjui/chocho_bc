from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['image', 'name', 'cost']
        
    def validate_cost(self, cost: str):
        try:
            c = float(cost)
            return str(c)
        except Exception as e:
            print(e)
            serializers.ValidationError(str(e))    

