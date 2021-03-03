from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def auth_login(request):
    return render(request,'authenticate/login.html')
def auth_registration(request):
    if request.method=='POST':
        mobile_phone = request.POST['mobile_phone']
        password = request.POST['user_password']
        confirm_password = request.POST['user_conf_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'You are already registered with this phone number')
    return render(request,'authenticate/registration.html')
