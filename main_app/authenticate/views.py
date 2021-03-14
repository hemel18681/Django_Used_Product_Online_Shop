from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from authenticate.models import user_info
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from main_app.settings import EMAIL_HOST_USER
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from PIL import Image

def auth_login(request):
    try:
        if request.session['user_name'] is not None:
            messages.error(request,'You are already logged in.')
            return redirect('home_page')
        else:
            if request.method=='POST':
                user_phone_number = int(request.POST['mobile_phone'])
                user_password = request.POST['user_password']
                try:
                    print(user_phone_number)
                    print(user_password)
                    if user_info.objects.filter(user_phone_number=int(user_phone_number), user_password = user_password ).exists():
                        author = user_info.objects.filter(user_phone_number=int(user_phone_number) )
                        details = author.values()
                        user_name = details[0]['user_name']
                        request.session['user_name'] = user_name
                        return redirect('home_page')   
                    else:
                        messages.error(request,'Phone Number or Password is wrong')
                        return render(request,'authenticate/login.html')
                except:
                    messages.error(request,'Phone Number or Password is wrong')
                    return render(request,'authenticate/login.html')
    except:
            if request.method=='POST':
                user_phone_number = int(request.POST['mobile_phone'])
                user_password = request.POST['user_password']
                try:
                    print(user_phone_number)
                    print(user_password)
                    if user_info.objects.filter(user_phone_number=int(user_phone_number), user_password = user_password ).exists():
                        author = user_info.objects.filter(user_phone_number=int(user_phone_number) )
                        details = author.values()
                        user_name = details[0]['user_name']
                        request.session['user_name'] = user_name
                        return redirect('home_page')   
                    else:
                        messages.error(request,'Phone Number or Password is wrong')
                        return render(request,'authenticate/login.html')
                except:
                    messages.error(request,'Phone Number or Password is wrong')
                    return render(request,'authenticate/login.html')
    return render(request,'authenticate/login.html')
def auth_registration(request):
    try:
        if request.session['user_name'] is not None:
            messages.error(request,'You are already logged in.')
            return redirect('home_page')
    except:
            if request.method=='POST':
                user_name = request.POST['user_name']
                user_phone_number = request.POST['mobile_phone']
                user_mail = request.POST['user_mail']
                user_password = request.POST['user_password']
                user_confirm_password = request.POST['user_confirm_password']
                if user_info.objects.filter(user_phone_number=user_phone_number).exists():
                    messages.error(request,'You are already registered with this phone number.')
                elif user_info.objects.filter(user_name=user_name).exists():
                    messages.error(request,'This username has already been used try new one.')
                elif user_info.objects.filter(user_mail=user_mail).exists():
                    messages.error(request,'You are already registered with this phone number.')
                elif user_password != user_confirm_password:
                    messages.error(request,'password and confirm password not matched')
                elif len(user_password)<6:
                    messages.error(request,'password length cannot have less than 6 digits')
                else:
                    saverecord = user_info()
                    saverecord.user_phone_number = user_phone_number
                    saverecord.user_name = user_name
                    saverecord.user_mail = user_mail
                    saverecord.user_password = user_password
                    saverecord.save()
                    messages.success(request,"you have been registerd successfully.")
                    return render(request,'authenticate/login.html')             
    return render(request,'authenticate/registration.html')


def auth_logout(request):
    request.session['user_name']  = None
    return redirect('login_page')

def forget_password(request):
    if request.method=='POST':
        user_phone_number = request.POST['mobile_phone']
        user_mail = request.POST['user_mail']
        if user_info.objects.filter(user_phone_number=user_phone_number, user_mail = user_mail).exists():
            author = user_info.objects.filter(user_phone_number=int(user_phone_number) )
            details = author.values()
            user_password = details[0]['user_password']
            subject = 'Forget Password of WA_x0r_AC'
            message = 'Your Password is "' + str(user_password) + '"(without quotes). We are recommanding you to change your password after login.'
            recepient = str(user_mail)
            send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently= False)
            messages.success(request,"Cheak Your mail to login.")
            return render(request,'authenticate/login.html')
        else:
            messages.success(request,"You are not registered. You can register yourself.")
            return render(request,'authenticate/registration.html')
    return render(request,'authenticate/password_reset.html')


def user_edit_profile(request):
    if request.method=='POST' and request.POST['user_picture_file']:
        myfile = request.POST['user_picture_file']
        print(myfile)
        fs = FileSystemStorage()
        name = ContentFile("hudai")
        filename = fs.save(myfile,name)
        url = fs.url(filename)
        user_name = request.session['user_name']
        author = user_info.objects.get(user_name=user_name)
        author.user_password  = request.POST['user_password']
        author.user_picture = url
        author.save()
    elif request.method=='POST':
        user_name = request.session['user_name']
        author = user_info.objects.get(user_name=user_name)
        author.user_password  = request.POST['user_password']
        author.save()
    user_name = request.session['user_name']
    author = user_info.objects.filter(user_name=user_name)
    details = author.values()
    print(details)
    context = {
        'user_info': details
    }
    return render(request,'authenticate/edit_profile.html',context)