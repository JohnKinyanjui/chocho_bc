from django.urls import path
from .views import *

urlpatterns = [
    path('accountS', AccountView.as_view()),
    path('groups', AccountGroupView.as_view())
]
