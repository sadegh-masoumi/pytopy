"""
courses urls
"""

from django.urls import path

from . import views

urlpatterns = [
    path('courses', views.Courses.as_view(), name='courses'),

]
