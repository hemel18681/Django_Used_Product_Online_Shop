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