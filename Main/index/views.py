from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    #response_ret = http.HttpResponseForbidden('参数错误')
    #return response_ret
    return HttpResponse("Hello, world. You're at the polls index.")