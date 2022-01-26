"""
urls of app_user
"""

from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout_user, name='logout'),
    # path('verify-email', views.login_user, name='verify-email'),
]
