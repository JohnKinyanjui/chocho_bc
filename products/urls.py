from django.urls import path
from .views import *

urlpatterns = [
    path('products', ProductView.as_view()),
    path('orders', OrderView.as_view()),
    path('orderItems', OrderItemView.as_view()),
]
