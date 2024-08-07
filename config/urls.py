"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('pages.urls')),
    prefix_default_language=False
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
