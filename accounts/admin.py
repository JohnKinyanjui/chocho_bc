from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AccountModel)
admin.site.register(AccountGroup)
admin.site.register(AccountOtp)
admin.site.register(AccountGroupItem)