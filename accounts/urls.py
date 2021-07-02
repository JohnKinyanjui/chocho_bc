from django.urls import path
from .views import *

urlpatterns = [
    path('otp', OtpView.as_view()),
    path('accounts', AccountView.as_view()),
    path('groups', AccountGroupView.as_view()),
    path('group/items', AccountGroupItemView.as_view())
]
