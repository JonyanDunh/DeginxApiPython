from django import forms
from django.core.exceptions import ValidationError
from App.Http.Forms.BaseJsonForm import BaseJsonForm
class Form(BaseJsonForm):
    username = forms.CharField(label="username", error_messages={"required": "This field cannot be empty!"})
    #password = forms.IntegerField(label="password")
    #email = forms.DecimalField(label="email")