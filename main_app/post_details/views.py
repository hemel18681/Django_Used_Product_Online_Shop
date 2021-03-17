from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from authenticate.models import user_info
from post_details.models import pending_post
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from main_app.settings import EMAIL_HOST_USER
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from PIL import Image
from .forms import make_post_form


def check_post(request):
    user_name = request.session['user_name']
    author = user_info.objects.filter(user_name=user_name)
    details = author.values()
    phone_number = details[0]['user_phone_number']
    set_size = pending_post.objects.filter(user_phone_number=phone_number)
    if set_size.count()== int(0):
            if request.method=='POST':
                form = make_post_form(request.POST, request.FILES)
                if form.is_valid:
                    print(request.POST['user_phone_number'])
                    if user_info.objects.filter(user_name=user_name, user_password = request.POST['user_password']).exists():
                        form.save()
                        return redirect('home_page')
                    else:
                        messages.error(request,'username or password is wrong')
                        form = make_post_form()
                        context = {
                            'form': form,
                        }
                        return render(request,'post_manage/make_post.html',context)
            else:
                form = make_post_form()
                context = {
                    'form': form,
                }
            return render(request,'post_manage/make_post.html',context)
    else:
        return render(request,'post_manage/wait_post.html')


# def all_post(request):
#     user_name = request.session['user_name']
#     author = user_info.objects.filter(user_name=user_name)
#     details = author.values()
#     phone_number = details[0]['user_phone_number']
#     set_size = pending_post.objects.filter(user_phone_number=phone_number)
#     if set_size.count()== int(0):
#         messages.error(request,'You don\'t have any post right now')
#         return render(request,'post_manage/all_post_list.html')
#     else:
#         return render()

