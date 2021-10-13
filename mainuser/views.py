from django.shortcuts import render,redirect
from django.http import request, HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Products
# Create your views here.


def adminlogin(request):
    if request.session.has_key('username'):
        return redirect('display')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
    
            check_user = auth.authenticate(username=email, password=password)
            user = User.objects.get(username=email)
            if check_user and user.is_superuser:
              
              username = user.id
              request.session['username'] = username
             
              return JsonResponse(
                   {"success": 'pass'},
                   safe=False
                 )
            else:
                return JsonResponse(
                   {"success": 'error'},
                   safe=False)
    
        else:
            return render(request, 'account/adminlogin.html')
    


def logout(request):
    try:
       request.session.flush()
    except:
        return redirect('adminlogin')
    return redirect("adminlogin")

def display(request):
    if request.session.has_key('username'):
        users = User.objects.all()
        return render(request, 'adminside/display.html',{"users":users})
    else:   
        return render(request, 'account/adminlogin.html')


def delete(request,username):
    if request.session.has_key('username'):
        print(username)
        u = User.objects.get(username = username)
        u.delete()
        return redirect("display")
    else:   
        return render(request, 'account/adminlogin.html')

def update(request,username):
    if request.session.has_key('username'):
        u = User.objects.get(username = username)
        if request.method =='POST':
           name = request.POST['name']
           email = request.POST['email']
           username = request.POST['username']
           u.first_name = name
           u.email = email
           u.username = username
           u.save()
           return redirect("display")
        else:
            name= u.first_name 
            username:u.username
            email = u.email
            return render(request, 'adminside/update.html',{'name':name,'email':email,'username':username})
    else:   
         return render(request, 'account/adminlogin.html')

def product(request):
    if request.session.has_key('username'):
        items = Products.objects.all()
        return render(request, 'adminside/product.html',{"items":items})
    else:   
         return render(request, 'account/adminlogin.html')

def deleteproduct(request,id):
    if request.session.has_key('username'):
        u = Products.objects.get(id = id)
        u.delete()
        return redirect("product")
    else:   
         return render(request, 'account/adminlogin.html')

def updateproduct(request,id):
    if request.session.has_key('username'):
        u = Products.objects.get(id = id)
        if request.method =='POST':
           name = request.POST['name']
           desc = request.POST['desc']
           price = request.POST['price']
           offer= request.POST['offer']
           print("before ")
           if len(request.FILES['img']) != 0:
               img= request.FILES['img']
               print("Success ")
               u.img  = img
              
           print(offer)
           u.name = name 
           u.desc = desc
           u.price = price
           
    
           u.save()
           return redirect("product")
        else:
            name= u.name 
            desc=u.desc
            price= u.price
            img = u.img
            offer = u.offer
            return render(request, 'adminside/p_update.html',{'name':name,'price':price,'desc':desc,'offer':offer,'img':img})
    else:   
         return render(request, 'account/adminlogin.html')


def additem(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            name = request.POST['name']
            desc = request.POST['desc']
            price = request.POST['price']
            offer= request.POST['offer']
            print("before ")
            if len(request.FILES['img']) != 0:
                img= request.FILES['img']
                print("Success ")
            u = Products.objects.create(name=name,desc=desc,price=price,img=img)
            u.save()
            return redirect("product")
        else:
            return render(request,'adminside/p_add.html')
    else:   
         return render(request, 'account/adminlogin.html')