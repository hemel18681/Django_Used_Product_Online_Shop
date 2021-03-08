from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from authenticate.models import user_info

def auth_login(request):
    if request.method=='POST':
        user_phone_number = request.POST['mobile_phone']
        user_password = request.POST['user_password']
        
        if user_info.objects.filter(user_phone_number=user_phone_number,user_password = user_password ).exists():
            author = user_info.objects.filter(user_phone_number=user_phone_number,user_password = user_password )
            details = author.values()
            info = list(details) 
            user_name = details[0]['user_name']
            user_password = details[0]['user_password']
            request.session['user_name'] = user_name
            return redirect('home_page')
        else:
            messages.error(request,'Phone Number or Password is wrong')
    return render(request,'authenticate/login.html')
def auth_registration(request):
    if request.method=='POST':
        user_name = request.POST['user_name']
        user_phone_number = request.POST['mobile_phone']
        user_mail = request.POST['user_mail']
        user_password = request.POST['user_password']
        user_confirm_password = request.POST['user_confirm_password']
        user = authenticate(request, user_phone_number=user_phone_number)
        user2 = authenticate(request, user_mail=user_mail)
        if user_info.objects.filter(user_phone_number=user_phone_number).exists():
            messages.error(request,'You are already registered with this phone number.')
        elif user_info.objects.filter(user_mail=user_mail).exists():
            messages.error(request,'You are already registered with this phone number.')
        elif user_password != user_confirm_password:
            messages.error(request,'password and confirm password not matched')
        elif len(user_password)<6:
            messages.error(request,'password length cannot have less than 6 digits')
        else:
            saverecord = user_info()
            saverecord.user_name = user_name
            saverecord.user_mail = user_mail
            saverecord.user_password = user_password
            saverecord.user_phone_number = user_phone_number
            saverecord.save()
            messages.success(request,"you have been registerd successfully.")
            return render(request,'authenticate/registration.html')              
    return render(request,'authenticate/registration.html')


def auth_logout(request):
    del request.session['user_name']
    return redirect('login_page')

# def forgot_password(request):
#     if request.method == 'POST':
#         return password_reset(request, 
#             from_email=request.POST.get('email'))
#     else:
#         return render(request, 'forgot_password.html')