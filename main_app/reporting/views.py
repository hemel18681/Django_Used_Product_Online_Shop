from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from authenticate.models import user_info
from post_details.models import pending_post, running_post
from .models import selling_report
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from main_app.settings import EMAIL_HOST_USER
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from PIL import Image
import _datetime
from datetime import timedelta
from django.utils import timezone


def check_report(request):
    if request.method=="POST":
        formdate = request.POST['formdate']
        todate = request.POST['todate']
        reports=selling_report.objects.filter(selling_date__lte=todate,selling_date__gte=formdate)
    else:
        reports=selling_report.objects.all()
    context = {
        'all_post':reports,
    }
    return render(request,'selling_report.html',context) 

