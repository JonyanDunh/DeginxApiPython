from django.urls import path, include

urlpatterns = [
    path('login/', include('App.Routes.Accounts.Login.urls')),
    path('register/', include('App.Routes.Accounts.Register.urls')),
    path('token/', include('App.Routes.Accounts.Token.urls')),
]