"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from core.settings import development

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('app_home.urls')),
    path('', include('app_user.urls')),
    path('', include('app_course.urls')),
    path('', include('app_contact_us.urls')),
    path('', include('app_article.urls')),
    path('', include('app_work_with_us.urls')),
    path('', include('app_about_us.urls')),
    path('', include('app_dashboard.urls'))
]

if True if os.environ.get('DEBUG') == 'True' else False:
    # add root static files
    urlpatterns = urlpatterns + static(development.STATIC_URL, document_root=development.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(development.MEDIA_URL, document_root=development.MEDIA_ROOT)
