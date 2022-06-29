from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import django.http
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from App.Http.Forms import Login
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
import json
from App.Actions.Convert import UserModelToJson
import datetime
@csrf_exempt
def login(request):
    if request.method == "GET":
        return HttpResponse("This page only supports POST mode", status=403)
    else:
        form = Login.Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data.get("username"), password=data.get("password"))
            if user is not None:
                django_login(request, user)
                print(user.__dict__)
                user_json =UserModelToJson.GetJson(user)
                return JsonResponse(user_json,safe=False)
            else:
                return HttpResponse("",status=454)
        else:
            print(form.errors_information())
            return JsonResponse(form.errors_information(), status=419)

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)
