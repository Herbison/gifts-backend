from django.urls import path
from .views import get_gifts_self, get_gifts_other, get_all_members, manage_gift

urlpatterns = [
    path('get_gifts_self/<int:member_id>/', get_gifts_self, name='get_gifts_self'),
    path('get_gifts_other/<int:member_id>/', get_gifts_other, name='get_gifts_other'),
    path('get_all_members/', get_all_members, name='get_all_members'),
    path('manage_gift/', manage_gift, name='manage_gift'),
]