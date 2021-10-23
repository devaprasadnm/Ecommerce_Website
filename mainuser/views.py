from django.shortcuts import render,redirect
from django.http import request, HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Products,Category,Order
# Create your views here.


def adminlogin(request):
    if request.session.has_key('id'):
        return redirect('display')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
    
            check_user = auth.authenticate(username=email, password=password)
            user = User.objects.get(username=email)
            if check_user and user.is_superuser:
              
              username = user.id
              request.session['id'] = username
             
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
    if request.session.has_key('id'):

        if request.method == 'POST':

            search =  request.POST['q'] 
            users = User.objects.filter(
            first_name__icontains=search)|User.objects.filter(
            email__icontains=search)|User.objects.filter(
            username__icontains=search)|User.objects.filter(
            last_name__icontains=search)
        else:     
            users = User.objects.all()

        paginator=Paginator(users,5)
        page = request.GET.get('page')
        users=paginator.get_page(page)
        return render(request, 'adminside/display.html',{"users":users})
    else:   
        return render(request, 'account/adminlogin.html')


def delete(request,username):
    if request.session.has_key('id'):
        print(username)
        u = User.objects.get(username = username)
        u.delete()
        return redirect("display")
    else:   
        return render(request, 'account/adminlogin.html')

def update(request,username):
    if request.session.has_key('id'):
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
    if request.session.has_key('id'):
        if request.method == 'POST':

            search =  request.POST['q'] 
            items = Products.objects.filter(
            name__icontains=search)
        else:     
            items = Products.objects.all()

        paginator=Paginator(items,5)
        page = request.GET.get('page')
        products=paginator.get_page(page)
        return render(request, 'adminside/product.html',{"items":products})
    else:   
         return render(request, 'account/adminlogin.html')

def deleteproduct(request,id):
    if request.session.has_key('id'):
        u = Products.objects.get(id = id)
        u.delete()
        return redirect("product")
    else:   
         return render(request, 'account/adminlogin.html')

def updateproduct(request,id):
    if request.session.has_key('id'):
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
    if request.session.has_key('id'):
        if request.method == 'POST':
            name = request.POST['name']
            desc = request.POST['desc']
            price = request.POST['price']
            offers= request.POST['offers']
            category = request.POST['category']
            if len(request.FILES['img']) != 0:
                img= request.FILES['img']
            c =Category.objects.get(category_name=category)
            u = Products.objects.create(name=name,desc=desc,price=price,img=img,offer=offers,category=c)
            u.save()
            return redirect("product")
        else:
            c=Category.objects.all()
            return render(request,'adminside/p_add.html',{'categories':c})
    else:   
         return render(request, 'account/adminlogin.html')


def orderdisplay(request):
    if request.session.has_key('id'):

        if request.method == 'POST':
            search =  request.POST['q'] 
            order = Order.objects.filter(
            name__icontains=search)
        else:     
            order = Order.objects.all()

        paginator=Paginator(order,5)
        page = request.GET.get('page')
        order=paginator.get_page(page)
        return render(request, 'adminside/order.html',{"order":order})
    else:   
        return render(request, 'account/adminlogin.html')

