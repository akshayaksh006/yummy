from django.urls import path
from userapp import views

urlpatterns=[
    path("home",views.home,name="home"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register")
]