from django.urls import path
from .views import get_gifts_self, get_gifts_other, get_all_members, add_gift, edit_gift_by_id,  get_gift_by_id, delete_gift_by_id, health_check

urlpatterns = [
    path('get_gifts_self/<int:member_id>/', get_gifts_self, name='get_gifts_self'),
    path('get_gifts_other/<int:member_id>/', get_gifts_other, name='get_gifts_other'),
    path('get_all_members/', get_all_members, name='get_all_members'),
    path('add_gift/', add_gift, name='add_gift'),
    path('edit_gift_by_id/<int:gift_id>/', edit_gift_by_id, name='edit_gift_by_id'),
    path('get_gift_by_id/<int:gift_id>/', get_gift_by_id, name='get_gift_by_id'),
    path('delete_gift_by_id/<int:gift_id>/', delete_gift_by_id, name='delete_gift_by_id'),
    path('health/', health_check, name='health_check'),
]