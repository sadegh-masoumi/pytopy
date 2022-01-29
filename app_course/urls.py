"""
courses urls
"""

from django.urls import path

from . import views

urlpatterns = [
    path('courses', views.Courses.as_view(), name='courses'),

    path('course/<int:pk>/<slug:slug>', views.view_single_course, name='single-curse')
]
