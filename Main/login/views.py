from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import django.http
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import sys

sys.path.append("..")
from Main.CosmosDB import action as CosmosDB
from Main.Action import encrypt

@csrf_exempt
def login(request):
    user ={}
    if request.POST:
        user['username'] = request.POST['username']
        #user['email'] = request.POST['email']
        #user['password'] = request.POST['password']
    return JsonResponse(CosmosDB.get_user(user))