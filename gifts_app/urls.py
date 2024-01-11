from django.urls import path
from .views import get_all_gifts


urlpatterns = [
    path('get_all_gifts/', get_all_gifts, name='get_all_gifts'),
]
