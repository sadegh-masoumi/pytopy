from django.shortcuts import render
from django.views.generic import TemplateView


def page_404(request, exception):
    print(exception)
    print()
    contex = {
        'exception': exception
    }
    return render(request, '404_page.html', contex)
