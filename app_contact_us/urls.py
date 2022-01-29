"""
contact_us urls
"""

from django.urls import path

from . import views

urlpatterns = [
    path('contact_us', views.contact_us, name='contact-us'),

]
