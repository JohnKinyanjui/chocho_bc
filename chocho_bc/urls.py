"""
chocho_bc URL Configuration
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from chocho_bc import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('products.urls')),
    path('', include('orders.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
