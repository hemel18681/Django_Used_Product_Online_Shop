from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from authenticate.models import user_info
from post_details.models import pending_post, running_post


def home(request):
    all_post = running_post.objects.all()
    context = {
        'all_post':all_post,
    }
    return render(request,'index.html',context)
    

def admin_page(request):
    return redirect('/admin/')

def post_view(request,post_id):
    user_name = request.session['user_name']
    if user_name is None:
        messages.success(request, "Please login first.");
        return render(request, 'authenticate\login.html')
    id = post_id
    post_details = running_post.objects.filter(id=id)
    details = post_details.values()
    print(details)
    user_phone_number = details[0]['user_phone_number']
    user_details = user_info.objects.filter(user_phone_number = user_phone_number)
    context = {
        'post_details':post_details,
        'user_details':user_details,
    }
    return render(request,'post_preview.html',context)

def indivisual_view_pic(request,post_id):
    id = post_id
    post_details = running_post.objects.filter(id=id)
    details = post_details.values()
    context = {
        'post_details':post_details,
    }
    return render(request,'full_picture.html',context)

