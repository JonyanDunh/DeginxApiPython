from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import sys
sys.path.append("..")
from Main.CosmosDB import action as CosmosDB
from Main.Action import encrypt
@csrf_exempt
def register(request):
    user ={}
    if request.POST:
        user['username'] = request.POST['username']
        user['email'] = request.POST['email']
        user['password'] = request.POST['password']
        CosmosDB.create_user(user)
        
    return HttpResponse(CosmosDB.get_user(user))
    #return HttpResponse(CosmosDB.get_user_uuid(user))