from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: Request):
    return HttpResponse('Hello world!')
