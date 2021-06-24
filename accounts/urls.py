from django.urls import path
from .views import *

urlpatterns = [
    path('accountS', AccountView.as_view()),
    path('groups', AccountGroupView.as_view()),
    path('group/items', AccountGroupItemView.as_view())
]
