"""
chocho_bc URL Configuration
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from chocho_bc import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
