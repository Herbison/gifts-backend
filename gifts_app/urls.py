from django.urls import path
from .views import get_all_gifts, get_all_members, create_gift


urlpatterns = [
    path('get_all_gifts/', get_all_gifts, name='get_all_gifts'),
    path('get_all_members/', get_all_members, name='get_all_members'),
    path('create_gift/', create_gift, name='create_gift'),
]
