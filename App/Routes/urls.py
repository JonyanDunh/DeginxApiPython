from django.urls import path, include

urlpatterns = [
    path('index/', include('App.Routes.Index.urls')),
    path('accounts/', include('App.Routes.Accounts.urls')),
    path('platform/', include('App.Routes.Platform.urls')),
]