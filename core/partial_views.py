from django.shortcuts import render


def header_home(request, **kwargs):
    return render(request, '_Header_Home.html', )


def header_light(request, **kwargs):
    return render(request, '_Header_Light.html')


def footer(request, **kwargs):
    return render(request, '_Footer.html')


def handler404(request, *args, **argv):
    return render(request, '404_page.html')
