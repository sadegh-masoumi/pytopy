"""
urls of app_work_with_us
"""

from . import views
from django.urls import path

urlpatterns = [
    path('work-with-us', views.WorkWithUsView.as_view(),name='work-with-us'),
]
