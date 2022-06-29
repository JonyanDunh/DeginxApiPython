# DeginxApiServer
 
App/
┣ Account/
┃ ┣ __pycache__/
┃ ┃ ┣ __init__.cpython-39.pyc
┃ ┃ ┣ admin.cpython-39.pyc
┃ ┃ ┣ apps.cpython-39.pyc
┃ ┃ ┗ models.cpython-39.pyc
┃ ┣ migrations/
┃ ┃ ┣ __pycache__/
┃ ┃ ┃ ┣ 0001_initial.cpython-39.pyc
┃ ┃ ┃ ┣ 0002_auto_20220629_1312.cpython-39.pyc
┃ ┃ ┃ ┣ 0003_usermodel_delete_user.cpython-39.pyc
┃ ┃ ┃ ┣ 0004_auto_20220629_1315.cpython-39.pyc
┃ ┃ ┃ ┣ 0005_usermodel_wechat.cpython-39.pyc
┃ ┃ ┃ ┣ 0006_auto_20220629_1323.cpython-39.pyc
┃ ┃ ┃ ┣ 0007_usermodel_avatar_usermodel_phone_and_more.cpython-39.pyc
┃ ┃ ┃ ┣ 0008_auto_20220629_1331.cpython-39.pyc
┃ ┃ ┃ ┣ 0009_usermodel_qq_alter_usermodel_avatar.cpython-39.pyc
┃ ┃ ┃ ┣ 0010_auto_20220629_1518.cpython-39.pyc
┃ ┃ ┃ ┣ 0011_usermodel_token_usermodel_user_uuid.cpython-39.pyc
┃ ┃ ┃ ┗ __init__.cpython-39.pyc
┃ ┃ ┣ 0001_initial.py
┃ ┃ ┣ 0002_auto_20220629_1312.py
┃ ┃ ┣ 0003_usermodel_delete_user.py
┃ ┃ ┣ 0004_auto_20220629_1315.py
┃ ┃ ┣ 0005_usermodel_wechat.py
┃ ┃ ┣ 0006_auto_20220629_1323.py
┃ ┃ ┣ 0007_usermodel_avatar_usermodel_phone_and_more.py
┃ ┃ ┣ 0008_auto_20220629_1331.py
┃ ┃ ┣ 0009_usermodel_qq_alter_usermodel_avatar.py
┃ ┃ ┣ 0010_auto_20220629_1518.py
┃ ┃ ┣ 0011_usermodel_token_usermodel_user_uuid.py
┃ ┃ ┗ __init__.py
┃ ┣ __init__.py
┃ ┣ admin.py
┃ ┣ apps.py
┃ ┣ models.py
┃ ┣ tests.py
┃ ┗ views.py
┣ Actions/
┃ ┣ Convert/
┃ ┃ ┣ __pycache__/
┃ ┃ ┃ ┗ UserModelToJson.cpython-39.pyc
┃ ┃ ┗ UserModelToJson.py
┃ ┣ Encrypt/
┃ ┃ ┣ __pycache__/
┃ ┃ ┃ ┗ encrypt.cpython-39.pyc
┃ ┃ ┗ encrypt.py
┃ ┣ Oauth/
┃ ┃ ┗ Authenticate/
┃ ┃   ┗ __pycache__/
┃ ┃ ┃   ┗ authenticate.cpython-39.pyc
┃ ┗ __pycache__/
┃   ┗ encrypt.cpython-39.pyc
┣ Core/
┃ ┣ __pycache__/
┃ ┃ ┣ __init__.cpython-39.pyc
┃ ┃ ┣ settings.cpython-39.pyc
┃ ┃ ┣ urls.cpython-39.pyc
┃ ┃ ┣ views.cpython-39.pyc
┃ ┃ ┗ wsgi.cpython-39.pyc
┃ ┣ __init__.py
┃ ┣ asgi.py
┃ ┣ settings.py
┃ ┣ urls.py
┃ ┣ views.py
┃ ┗ wsgi.py
┣ Http/
┃ ┣ Forms/
┃ ┃ ┣ __pycache__/
┃ ┃ ┃ ┣ BaseJsonForm.cpython-39.pyc
┃ ┃ ┃ ┣ Login.cpython-39.pyc
┃ ┃ ┃ ┗ Register.cpython-39.pyc
┃ ┃ ┣ BaseJsonForm.py
┃ ┃ ┣ Login.py
┃ ┃ ┗ Register.py
┃ ┗ Middlewares/
┃   ┣ __pycache__/
┃ ┃ ┃ ┣ ExceptionMiddleware.cpython-39.pyc
┃ ┃ ┃ ┗ ResponseMiddleware.cpython-39.pyc
┃   ┣ ExceptionMiddleware.py
┃   ┗ ResponseMiddleware.py
┣ Routes/
┃ ┣ Accounts/
┃ ┃ ┣ Login/
┃ ┃ ┃ ┣ __pycache__/
┃ ┃ ┃ ┃ ┣ __init__.cpython-39.pyc
┃ ┃ ┃ ┃ ┣ urls.cpython-39.pyc
┃ ┃ ┃ ┃ ┗ views.cpython-39.pyc
┃ ┃ ┃ ┣ migrations/
┃ ┃ ┃ ┃ ┗ __init__.py
┃ ┃ ┃ ┣ __init__.py
┃ ┃ ┃ ┣ admin.py
┃ ┃ ┃ ┣ apps.py
┃ ┃ ┃ ┣ models.py
┃ ┃ ┃ ┣ tests.py
┃ ┃ ┃ ┣ urls.py
┃ ┃ ┃ ┗ views.py
┃ ┃ ┣ Register/
┃ ┃ ┃ ┣ __pycache__/
┃ ┃ ┃ ┃ ┣ __init__.cpython-39.pyc
┃ ┃ ┃ ┃ ┣ urls.cpython-39.pyc
┃ ┃ ┃ ┃ ┗ views.cpython-39.pyc
┃ ┃ ┃ ┣ migrations/
┃ ┃ ┃ ┃ ┗ __init__.py
┃ ┃ ┃ ┣ __init__.py
┃ ┃ ┃ ┣ admin.py
┃ ┃ ┃ ┣ apps.py
┃ ┃ ┃ ┣ models.py
┃ ┃ ┃ ┣ tests.py
┃ ┃ ┃ ┣ urls.py
┃ ┃ ┃ ┗ views.py
┃ ┃ ┣ Token/
┃ ┃ ┃ ┣ __pycache__/
┃ ┃ ┃ ┃ ┣ __init__.cpython-39.pyc
┃ ┃ ┃ ┃ ┣ urls.cpython-39.pyc
┃ ┃ ┃ ┃ ┗ views.cpython-39.pyc
┃ ┃ ┃ ┣ migrations/
┃ ┃ ┃ ┃ ┗ __init__.py
┃ ┃ ┃ ┣ __init__.py
┃ ┃ ┃ ┣ admin.py
┃ ┃ ┃ ┣ apps.py
┃ ┃ ┃ ┣ models.py
┃ ┃ ┃ ┣ tests.py
┃ ┃ ┃ ┣ urls.py
┃ ┃ ┃ ┗ views.py
┃ ┃ ┣ __pycache__/
┃ ┃ ┃ ┗ urls.cpython-39.pyc
┃ ┃ ┗ urls.py
┃ ┣ Index/
┃ ┃ ┣ __pycache__/
┃ ┃ ┃ ┣ __init__.cpython-39.pyc
┃ ┃ ┃ ┣ urls.cpython-39.pyc
┃ ┃ ┃ ┗ views.cpython-39.pyc
┃ ┃ ┣ migrations/
┃ ┃ ┃ ┗ __init__.py
┃ ┃ ┣ __init__.py
┃ ┃ ┣ admin.py
┃ ┃ ┣ apps.py
┃ ┃ ┣ models.py
┃ ┃ ┣ tests.py
┃ ┃ ┣ urls.py
┃ ┃ ┗ views.py
┃ ┣ Platform/
┃ ┃ ┣ __pycache__/
┃ ┃ ┃ ┣ __init__.cpython-39.pyc
┃ ┃ ┃ ┣ urls.cpython-39.pyc
┃ ┃ ┃ ┗ views.cpython-39.pyc
┃ ┃ ┣ migrations/
┃ ┃ ┃ ┗ __init__.py
┃ ┃ ┣ __init__.py
┃ ┃ ┣ admin.py
┃ ┃ ┣ apps.py
┃ ┃ ┣ models.py
┃ ┃ ┣ tests.py
┃ ┃ ┣ urls.py
┃ ┃ ┗ views.py
┃ ┣ __pycache__/
┃ ┃ ┗ urls.cpython-39.pyc
┃ ┗ urls.py
┣ Utils/
┃ ┗ __pycache__/
┃   ┣ RequestVerify.cpython-39.pyc
┃   ┣ enums.cpython-39.pyc
┃   ┣ exceptions.cpython-39.pyc
┃   ┣ middlewares.cpython-39.pyc
┃   ┣ result.cpython-39.pyc
┃   ┗ results.cpython-39.pyc
┣ Run.py
┗ settings.config