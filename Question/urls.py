from django.urls import path
from django import urls
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.questions, name='questions'),
    url(r'(?P<number>\d+)/$', views.square, name='square'),
    #url(r'(?P<num1>\d+)/(?P<num2>\d+)/$', views.addition, name='addition'),
]
