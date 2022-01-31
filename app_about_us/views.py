from django.shortcuts import render
from django.views.generic import TemplateView


class AboutUs(TemplateView):
    template_name = 'about_us.html'
