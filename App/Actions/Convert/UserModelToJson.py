from django.forms.models import model_to_dict
import json
import datetime
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

def GetJson(user):
    user_json =json.loads(json.dumps(model_to_dict(user),cls=DateEncoder))
    user_json["password"]=None
    return user_json

