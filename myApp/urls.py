from . import views
from django.urls import path
from .views import home, addItem



urlpatterns = [
    path("", views.home, name = "home"),
    path("Login/", views.Login, name='Login'),
    path("Order/", views.Login, name='Order'),
    path('createOrder/', views.Login, name='createOrder'),
    path("Menu/", views.Menu, name='Menu'),
    path("Admin/", views.Admin, name='Admin'),
    path('register/', views.register_view, name ="register"),
    path('addItem/', addItem, name='addItem'),
]