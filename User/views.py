from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from User.models import User
# Create your views here.

class UserList(ListView):
    model =User
    def get(self,request,*args,**kwargs):
        return HttpResponse("Hai pooja")
