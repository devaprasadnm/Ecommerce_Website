from django.shortcuts import render,redirect
from django.http import request, HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.


def adminlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        check_user = auth.authenticate(username=email, password=password)
        user = User.objects.get(username=email)
        if check_user and user.is_superuser:
          
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
        return render(request, 'account/adminlogin.html')

def logout(request):
    try:
       request.session.flush()
    except:
        return redirect('adminlogin')
    return redirect("adminlogin")

def display(request):
    return render(request, 'display.html')