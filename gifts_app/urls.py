from django.urls import path
from .views import get_all_gifts, get_all_members


urlpatterns = [
    path('get_all_gifts/', get_all_gifts, name='get_all_gifts'),
    path('<get_all_members/', get_all_members, name='meet_results'),
]
