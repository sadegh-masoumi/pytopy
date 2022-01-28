"""
urls of app_user
"""
from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),

    path('register', views.register_user, name='register'),
    path('verify-email', views.registered, name='registered'),

    path('logout', views.logout_user, name='logout'),

    path('verify-email/<int:pk>/<token>', views.verify_email, name='verify-email'),

    path('password-recovery', views.forget_password, name='forget-password'),
    path('password-recovery/<int:pk>/<token>', views.password_recovery, name='password-recovery'),
]
