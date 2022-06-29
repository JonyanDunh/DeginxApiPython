from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import jwt
import time
from configparser import RawConfigParser
config = RawConfigParser()
config.read('./settings.config')

@login_required
def token(request):
    jwt_secret=config.get('token_jwt','JWT_SECRET')
    jwt_token = jwt.encode({"username": request.user.username,"user_uuid":request.user.user_uuid,"exp":int(time.time())+3600}, jwt_secret, algorithm="HS256")
    print(jwt.decode(jwt_token, jwt_secret, algorithms=["HS256"]))
    return HttpResponse(jwt_token)