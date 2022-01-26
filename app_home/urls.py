"""
urls of app_home
"""
from .views import Home
from django.urls import path

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
