"""
urls of app_article
"""
from django.urls import path

from . import views

urlpatterns = [
    path('articles', views.view_articles, name='articles'),

]
