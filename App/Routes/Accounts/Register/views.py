from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from App.Http.Forms import Register
from django.contrib.auth.models import User
from Account.models import UserModel
from django.contrib.auth import login
from App.Actions.Convert import UserModelToJson
import uuid
@csrf_exempt
def register(request):
    if request.method == "GET":
        return HttpResponse("This page only supports POST mode", status=403)
    else:
        form = Register.Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = UserModel.objects.filter(username=data.get(
                "username"))
            if not user.exists():
                user = UserModel.objects.create_user(username=data.get(
                    "username"), password=data.get("password"), email=data.get("email"),user_uuid=str(uuid.uuid4()))
                if user is not None:
                    login(request, user)
                    user_json =UserModelToJson.GetJson(user)
                    return JsonResponse(user_json)
                else:
                    return HttpResponse("", status=453)
            else:
                return HttpResponse("Please change your username and register or log in directly", status=452)

        else:
            print(form.errors_information())
            return JsonResponse(form.errors_information(), status=419)
