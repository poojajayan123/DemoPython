from django.urls import path
from django import urls
from django.conf.urls import url
from User.views import UserList
from . import views

urlpatterns = [
    path('',UserList.as_view(), name='Users'),
]
