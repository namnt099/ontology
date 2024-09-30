"""lasotuvi_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path

from lasotuvi_ontology import views as lstv
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'api_laso', lstv.api_laso),
    re_path(r'api_giaidoan', lstv.api_giaidoan),
    re_path(r'api_daivan', lstv.api_daivan),
    re_path(r'^api_vanhan', lstv.api_vanhan),
    re_path(r'^api_trondoi', lstv.api_trondoi),
    re_path(r'^api_convertPdf', lstv.api_convertPdf),
    re_path(r'^$', csrf_exempt(lstv.lasotuvi_django_index)),
    path('pdf/', lstv.GeneratePdf.as_view()),
]


