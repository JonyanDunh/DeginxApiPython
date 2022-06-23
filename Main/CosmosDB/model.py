import datetime
from Main.Action import encrypt



def default_user_model(user):
    # notice new fields have been added to the sales order
    user_information = {'id' : encrypt.md5_hash(user["email"]),
            'email' : user["email"],
            'password' : encrypt.md5_hash(user["password"])
            }

    return user_information