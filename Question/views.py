from django.shortcuts import render
from http import HTTPStatus
from urllib import request


def home(request):
    # response = requests.get('http://freegeoip.net/json/')
    # geodata = response.json()
    response = "Hai pooja"
    return render(request, 'core/core.html', response)
