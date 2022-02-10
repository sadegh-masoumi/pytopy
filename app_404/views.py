from django.shortcuts import render
from django.views.generic import TemplateView


def page_404(request, exception):
    contex = {
        'exception': exception
    }
    return render(request, '404_page.html', contex)
