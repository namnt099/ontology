from django.contrib import admin
from django.urls import path, re_path
# from django.conf.urls import url

from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^api_laso', views.api_laso),
    re_path(r'^api_giaidoan', views.api_giaidoan),
    re_path(r'^api_daivan', views.api_daivan),
    re_path(r'^api_vanhan', views.api_vanhan),
    re_path(r'^api_trondoi', views.api_trondoi),
    re_path(r'^api_convertPdf', views.api_convertPdf),
    re_path(r'^$', csrf_exempt(views.lasotuvi_django_index)),
    path('pdf/', views.GeneratePdf.as_view()),
    #path('', views.abc, name='abc')
]
