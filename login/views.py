from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import  customer, admin, deliveryman, shop, location
from django.contrib import messages


def loc(request):
    Locations = location.objects.all()
    return render(request,'location.html',{'locations':Locations})

def register(request):
    Locations = location.objects.all()
    if request.method == 'POST' and request.POST.get('name') != "" and request.POST.get('address') != "" and request.POST.get('email') != "" and request.POST.get('password') != "":
        
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        loc = request.POST.get('loc')
       # checklog=request.POST.get('checklog')

        if request.POST.get('checklog')=='customer':
            
            """ saverecord= customer() """
            
            if customer.objects.filter(email=email).exists():
                messages.warning(request,"account already exists")
                return redirect('register',{'locations':Locations})
            else:
                saverecord= customer(name=name,address=address,phone=phone,email=email,password=password)
                saverecord.save()
                messages.success(request,'record saved')
                return redirect('login')

        if request.POST.get('checklog')=='deliveryman':
            
            """ saverecord= customer() """
            
            if deliveryman.objects.filter(email=email).exists():
                messages.warning(request,"account already exists")
                return redirect('register',{'locations':Locations})
            else:
                saverecord= deliveryman(name=name,address=address,phone=phone,email=email,password=password)
                saverecord.save()
                messages.success(request,'record saved')
                return render(request,'login.html')

        if request.POST.get('checklog')=='shop':
            
            """ saverecord= customer() """
            
            if shop.objects.filter(email=email).exists():
                messages.warning(request,"account already exists")
                return redirect('register',{'locations':Locations})
            else:
                saverecord= shop(name=name,address=address,phone=phone,email=email,password=password, loc_id=loc)
                saverecord.save()
                messages.success(request,'record saved')
                return render(request,'login.html')

        if request.POST.get('checklog')=='admin':
            
            """ saverecord= customer() """
            
            if admin.objects.filter(email=email).exists():
                messages.warning(request,"account already exists")
                return redirect('register',{'locations':Locations})
            else:
                saverecord= admin(name=name,address=address,phone=phone,email=email,password=password)
                saverecord.save()
                messages.success(request,'record saved')
                return render(request,'login.html')

        else:
            return redirect('register',{'locations':Locations})
        
        """ checklog = request.POST.get('checklog')
        p=customer(name = name, address = address, email = email, password = password, phone = phone)
        p.save() """
        
    else:
        return render(request,'register.html',{'locations':Locations})

def login(request):
    if request.method == 'POST' and request.POST.get('type')!="" and request.POST.get('checklog')!="" and request.POST.get('name')!="" and request.POST.get('password')!="":
        name=request.POST.get('name')
        password=request.POST.get('password')
        checklog = request.POST.get('checklog')
        if checklog == "customer" and customer.objects.filter(name=name,password=password).exists():
            messages.success(request,'login successful')
            return redirect('location')
        if checklog == "admin" and admin.objects.filter(name=name,password=password).exists():
            messages.success(request,'login successful')
            return redirect('login')
        if checklog == "deliveryman" and deliveryman.objects.filter(name=name,password=password).exists():
            messages.success(request,'login successful')
            return redirect('login')
        if checklog == "shop" and shop.objects.filter(name=name,password=password).exists():
            
            messages.success(request,'login successful')
            return redirect('login')
        else:
            messages.success(request,'Wrong username or password')
            return redirect('login')
    else:

        return render(request,'login.html')


