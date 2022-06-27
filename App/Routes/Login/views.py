from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import django.http
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import sys


from App.Utils.CosmosDB import action as CosmosDB
from App.Http.Forms import Login
@csrf_exempt
def login(request):
    if request.method == "GET":
        form = Login.Form()
        return render(request, "add_emp.html", {"form": form})
    else:
        form = Login.Form(request.POST)
        if form.is_valid():
            user ={}
            data = form.cleaned_data
            user['username'] = data.get("username")
            #user['email'] = data.get("email")
            #user['password'] = data.get("password")
            return JsonResponse(CosmosDB.get_user(user))
        else:
            print(form.errors_information())
            return JsonResponse(form.errors_information(),status=419)