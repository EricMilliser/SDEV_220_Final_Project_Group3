
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("myApp.urls")),
    path('users/', include("users.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
]
