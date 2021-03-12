from django.shortcuts import render
from http import HTTPStatus
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

@api_view(["GET"])
def questions(request):
    msg ="sample response"
    return JsonResponse(msg, content_type='text/json')


@api_view(["GET"])
def square(request,number):
    a =  int(number)
    print(number)
    square =  a**2
    msg = "Square of the given number {} is {}".format(a,square)
    return JsonResponse(msg, content_type='text/json',safe=False)

# @api_view(["GET"])
# def addition(request,num1,num2):
#     a =  int(num1)
#     b = int(num2)
#     msg = "Sum = {}".format(a+b)
#     return JsonResponse(msg, content_type='text/json',safe=False)