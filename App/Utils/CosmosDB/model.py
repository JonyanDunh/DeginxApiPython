import datetime
from App.Actions import encrypt
import uuid


def default_creat_user_model(user):
    # notice new fields have been added to the sales order
    user_information = {'id' : str(uuid.uuid4()),
            'username':user["username"],
            'email' : user["email"],
            'password' : encrypt.md5_hash(user["password"])
            }

    return user_information