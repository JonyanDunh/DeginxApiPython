from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    wechat = models.CharField(max_length=25, null=True)
    qq = models.CharField(max_length=25, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.CharField(max_length=200,null=True, blank=True,default="https://message.biliimg.com/bfs/im/5a7310c3a47c0b1ac6c9153b5aa84dd4bb641f8f.png")

    pass