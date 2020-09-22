from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("",home,name='home'),
    path("register/",register,name='register'),
    path("login/",LoginView.as_view(template_name='taskapp/form.html'),name="login"),
    path("logout/",LogoutView.as_view(template_name='taskapp/base.html'),name="logout"),
    path("create/",createContainers,name='create'),
    path('mycontainers/', MyContainers, name='mycontainers')

]