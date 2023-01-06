from django.shortcuts import render
from django.contrib import messages
from .models import Food
# Create your views here.
def home(request):
    return render(request,'index.html')
def login(request):
    if request.method=="POST":
        name2=request.POST['Username'];
        password3=request.POST['Password'];
        a=Food.objects.filter(name=name2,password=password3)
        if a.exists():
            messages.info(request,'login succesful')
            print("login successful")
        else:
            messages.info(request, 'invalid credentials')
            print("invalid credentials")
    return render(request,'login.html')
def register(request):
    if request.method == "POST":
        name1=request.POST['yourname'];
        email1=request.POST['email'];
        password1=request.POST['password'];
        password2=request.POST['passwords'];
        data=Food(name=name1,email=email1,password=password1)
        data.save()
        print("saved")
    else:
        print("not saved")

    return render(request,'register.html')