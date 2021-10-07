from django.shortcuts import render,redirect
from django.http import request, HttpResponse
from django.contrib.auth.models import User,auth
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        check_user = auth.authenticate(username=email, password=password)
        if check_user:
          user = User.objects.get(username=email)
          username = user.first_name
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
        del request.session['username']
    except:
        return redirect('login')
    return redirect("login")


def main(request):
    return render(request, 'main.html')

def adminlogin(request):
    if request.method== 'POST':

        email = request.POST['email']
        password = request.POST['password']

        check_user = auth.authenticate(username=email, password=password)
        
        if check_user:
          u = User.objects.get(username=email)
          Name=u.first_name
          request.session['username'] = Name
          return JsonResponse(

              {'success':True},
               safe=False
             )

        else:    
            
          return JsonResponse(
               {'success':False},
               safe=False
             )      

    else:
        return render(request, 'account/adminlogin.html') 