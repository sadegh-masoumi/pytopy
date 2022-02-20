from django.shortcuts import render
from django.http import HttpResponse
from core.settings.base import UPDATE_TOKEN


def update_project(request):
    if request.method == "POST":
        token = request.POST.get('Token')
        if token == UPDATE_TOKEN:
            pass

    else:
        HttpResponse('<h1>404</h1>')
