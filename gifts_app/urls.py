from django.urls import path
from .views import create_gift, get_self_view, get_other_view, update_gift, remove_gift


urlpatterns = [
    path('create/', create_gift, name='create_gift'),
]
