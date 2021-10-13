from django.shortcuts import render,redirect
from django.http import request, HttpResponse
from django.contrib.auth.models import User,auth
from django.core.paginator import Paginator
from django.http import JsonResponse
from mainuser.models import Products
# Create your views here.



def login(request):
    if request.session.has_key('username'):
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
    
            check_user = auth.authenticate(username=email, password=password)
            if check_user:
              user = User.objects.get(username=email)
              username = user.username
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
            return render(request, 'account/login.html')
    

def signup(request):
    if request.session.has_key('username'):
        return redirect('home')
    else:
        if request.method == 'POST':
    
            name = request.POST['name']
            password1 = request.POST['password']
            password2 = request.POST['repassword']
            email = request.POST['email']
            username = str(email)
            print("before ")
            if password1 == password2:
                print("pass crct ")
                if User.objects.filter(email=email).exists():
                    return JsonResponse(
                        {'success':'email_check'},
                        safe = False
                    )
                else:
                    
                    user = User.objects.create_user(first_name=name, username=username, password=password1, email=email)
                    user.save()
                    return JsonResponse(
                        {'success':'pass'},
                        safe = False
                    )
            else:
                return JsonResponse(
                        {'success':'password_check'},
                        safe = False
                    )
        else:
            return render(request,'account/signup.html')

def logout(request):
    try:
       request.session.flush()
    except:
        return redirect('login')
    return redirect("login")

def home(request):
    if request.session.has_key('username'):
        return redirect('userdisplay')
    else:
        items = Products.objects.all()
        return render(request, 'user/index.html',{'products':items,'name1':"login",'name2':"signup"})

def userdisplay(request):
    if request.session.has_key('username'):
        items = Products.objects.all()
        user = User.objects.get(username=request.session['username'])
        name = user.first_name 
        return render(request, 'user/index.html',{'products':items,'name1':name,'name2':"logout"})
    else:
        return redirect('home')