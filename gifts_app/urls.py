from django.urls import path
from .views import get_all_gifts_self, get_all_gifts_other, get_all_members, create_gift


urlpatterns = [
    path('get_all_gifts_self/', get_all_gifts_self, name='get_all_gifts_self'),
    path('get_all_gifts_other/', get_all_gifts_other, name='get_all_gifts_other'),
    path('get_all_members/', get_all_members, name='get_all_members'),
    path('create_gift/', create_gift, name='create_gift'),
]
