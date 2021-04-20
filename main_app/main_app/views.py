from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from authenticate.models import user_info
from django.core.mail import send_mail
from main_app.settings import EMAIL_HOST_USER
from post_details.models import pending_post, running_post, done_post
from reporting.models import selling_report
from django.http import JsonResponse
from decimal import Decimal
import json


def home(request):
    if request.method=='POST':
        print(str(request.POST['search_name']))
        namel = str(request.POST['search_name']).lower()
        nameu = str(request.POST['search_name']).upper()
        name = str(request.POST['search_name'])
        all_postl = running_post.objects.filter(post_title=namel)
        all_postu = running_post.objects.filter(post_title=nameu)
        all_posto = running_post.objects.filter(post_title=name)
        all_post = all_postl | all_posto | all_postu
    else:
        all_post = running_post.objects.all().order_by('post_given_date').reverse()
    
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
    service_charge = details[0]['post_money'] * Decimal( 0.05)
    main_price = details[0]['post_money'] *  Decimal( 0.95)
    service_charge = round(service_charge,2)
    main_price = round(main_price,2)
    print(details)
    user_phone_number = details[0]['user_phone_number']
    user_details = user_info.objects.filter(user_phone_number = user_phone_number)
    context = {
        'post_details':post_details,
        'user_details':user_details,
        'service_charge':service_charge,
        'main_price':main_price
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

def complete_payment_work(request,post_id):
    user_name = request.session['user_name']
    if user_name is None:
        messages.success(request, "Please login first.");
        return render(request, 'authenticate\login.html')
    id = int(post_id)
    post_details = running_post.objects.filter(id=id)
    details = post_details.values()
    service_charge = details[0]['post_money'] * Decimal( 0.05)
    main_price = details[0]['post_money'] *  Decimal( 0.95)
    service_charge = round(service_charge,2)
    main_price = round(main_price,2)
    print(details)
    user_phone_number = details[0]['user_phone_number']
    user_details = user_info.objects.filter(user_phone_number = user_phone_number)
    context = {
        'post_details':post_details,
        'user_details':user_details,
        'service_charge':service_charge,
        'main_price':main_price
    }
    return render(request,'confirm_payment.html',context)

def make_report(request):
    body = json.loads(request.body)
    post_id = body['product_id']
    id = int(post_id)
    post_details = running_post.objects.filter(id=id)
    details = post_details.values()
    print(details)
    seller_phone_number = details[0]['user_phone_number']
    user_name = request.session['user_name']
    buyer_det = user_info.objects.filter(user_name = user_name)
    buyer_details = buyer_det.values()
    seller_det = user_info.objects.filter(user_phone_number=seller_phone_number)
    seller_details = seller_det.values()
    seller_name = seller_details[0]['user_name']
    buyer_phone_number = buyer_details[0]['user_phone_number']
    selling_price = float(details[0]['post_money'])*0.95
    profit_price = float(details[0]['post_money'])*0.05
    saverecord = selling_report()
    saverecord.seller_phone_number = seller_phone_number
    saverecord.buyer_phone_number = buyer_phone_number
    saverecord.selling_price = selling_price
    saverecord.profit_price = profit_price
    saverecord.product_id = id
    saverecord.save()
    saverecord = done_post()
    saverecord.user_phone_number = details[0]['user_phone_number']
    saverecord.post_title = details[0]['post_title']
    saverecord.post_description = details[0]['post_description']
    saverecord.post_picture = details[0]['post_picture']
    saverecord.post_money = details[0]['post_money']
    saverecord.product_id = details[0]['id']
    saverecord.post_used_days = details[0]['post_used_days']
    saverecord.done_post = True
    saverecord.post_given_date = details[0]['post_given_date']
    saverecord.save()
    running_post.objects.filter(id=id).delete()
    subject = 'Sold Product from WA_x0r_AC'
    message = 'Your Product "' + str(details[0]['post_title']) + '"has been sold to User Name: ' + str(user_name) + ' Phone Number: ' + str(buyer_phone_number)
    user_mail = buyer_details[0]['user_mail']
    recepient = str(user_mail)
    send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently= False)
    subject = 'Purchase Product from WA_x0r_AC'
    message = 'Product "' + str(details[0]['post_title']) + '"has been sold to you by User Name: ' + str(seller_name) + ' Phone Number: ' + str(seller_phone_number)
    seller_mail = seller_details[0]['user_mail']
    recepient = str(seller_mail)
    send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently= False)
    return JsonResponse('Service Charge Complete', safe=False)

def thankyou(request):
    return render(request,'thankyou.html')


def search_product(request,search_name):
    name = search_name
    print(name)
    post_details = running_post.objects.filter(post_title=name)
    context = {
        'all_post':post_details,
    }
    return render(request,'search_page.html',context)