from django.urls import path
from .views import create_gift_self, create_gift_other, get_self_view, get_other_view, update_gift, remove_gift


urlpatterns = [
    path('create_gift_self/', create_gift_self, name='create_gift_self'),
    path('create_gift_other/', create_gift_other, name='create_gift_other'),
]
