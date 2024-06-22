"""
URL configuration for gifts_project project.
"""
from django.contrib import admin
from django.urls import path, include
from gifts_app.views import redirect_to_admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('gifts_app.urls')),
    path('', redirect_to_admin),
]
