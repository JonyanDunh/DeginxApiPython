from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from App.Http.Forms import Login,Register
import sys
from django.contrib import auth
from django.contrib.auth.models import User

def platform(request):
    if not request.user.is_authenticated:
        return HttpResponse("请登录")
        
    return HttpResponse("Hello~"+request.user.username)