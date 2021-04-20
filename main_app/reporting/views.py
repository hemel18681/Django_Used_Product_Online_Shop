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
from decimal import Decimal


def check_report(request):
    if request.method=="POST":
        formdate = request.POST['formdate']
        todate = request.POST['todate']
        if request.POST['option'] == "indivisuals" and request.POST['user_id'] is None:
            messages.error(request,'you entered indivisual but didn\'t gave any user id')
            reports=selling_report.objects.all()
        elif request.POST['option'] == "indivisualb" and request.POST['user_id'] is None:
            messages.error(request,'you entered indivisual but didn\'t gave any user id')
            reports=selling_report.objects.all()
        elif request.POST['option'] == "indivisuals" and request.POST['user_id'] is not None:
            reports=selling_report.objects.filter(seller_phone_number=int(request.POST['user_id']), selling_date__lte=todate,selling_date__gte=formdate)
        elif request.POST['option'] == "indivisualb" and request.POST['user_id'] is not None:
            reports=selling_report.objects.filter(buyer_phone_number=int(request.POST['user_id']), selling_date__lte=todate,selling_date__gte=formdate)
        else:
            reports=selling_report.objects.filter(selling_date__lte=todate,selling_date__gte=formdate)
    else:
        reports=selling_report.objects.all()
    total_earning = Decimal(0.0)
    for star in reports.iterator():
        total_earning = total_earning + star.profit_price
    total_earning = round(total_earning,2)
    context = {
        'all_post':reports,
        'total_earning':total_earning
    }
    return render(request,'selling_report.html',context) 

