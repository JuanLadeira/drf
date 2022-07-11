from . views import api_home
from django.urls import path

urlpatterns = [
    path('', api_home, name='api'),
]