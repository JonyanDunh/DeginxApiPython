from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from App.Http.Forms import Login
import sys
from django.contrib import auth
from django.contrib.auth.models import User
@csrf_exempt
def register(request):
    if request.method == "GET":
        return HttpResponse("This page only supports POST mode", status=403)
    else:
        form = Login.Form(request.POST)
        if form.is_valid():
            user = {}
            data = form.cleaned_data
            #user=authenticate(username=data.get("username"),password=data.get("password"))
            User.objects.create(username=data.get("username"),password=data.get("password"))
            print(user)
            #user['username'] = data.get("username")
            #user['email'] = data.get("email")
            #user['password'] = data.get("password")
            #return JsonResponse(CosmosDB.get_user(user))
        else:
            print(form.errors_information())
            return JsonResponse(form.errors_information(), status=419)