from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def token(request):
    return HttpResponse("fuck")