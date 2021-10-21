from django.shortcuts import render,redirect
from django.http import request, HttpResponse
from django.contrib.auth.models import User,auth
from django.core.paginator import Paginator
from django.http import JsonResponse
from mainuser.models import Products,Category,Cart,Order
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
        c=Category.objects.all()
        items = Products.objects.all()
        return render(request, 'user/index.html',{'products':items,'name1':"login",'name2':"signup",'categories':c})

def userdisplay(request):
    if request.session.has_key('username'):
        c=Category.objects.all()
        items = Products.objects.all()
        user = User.objects.get(username=request.session['username'])
        name = user.first_name 
        return render(request, 'user/index.html',{'products':items,'name1':name,'name2':"logout",'categories':c})
    else:
        return redirect('home')

def product(request,product_id):
    if request.session.has_key('username'):
        print(product_id)
        product = Products.objects.all()
        product_id =int(product_id)
        user = User.objects.get(username=request.session['username'])
        name = user.first_name 
        return render(request, 'user/product_details.html',{'product':product,'product_id':product_id,'name1':name,'name2':"logout"})
    else:
        return redirect('home')
        
def cart(request):
    if request.session.has_key('username'):
        u = User.objects.get(username=request.session['username'])
        if request.method == 'POST':
            product_id = request.POST['product_id']
            qty = request.POST['quantity']
            

            p = Products.objects.get(id=product_id)

            if Cart.objects.filter(pid=product_id):
                Cart.objects.filter(pid=product_id).update(qty=qty)
            else:
                c = Cart.objects.create(uid=u, pid=p ,qty=qty)
                c.save()
    
            return redirect('cart')
        else:
            c = Cart.objects.filter(uid=u.id)
            items = c.count()
            user = User.objects.get(username=request.session['username'])
            name = user.first_name 
            
            return render(request, 'user/cart.html',{'cart':c,'items':items,'name1':name,'name2':"logout"})
    else:
        return redirect('login')

def calc(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            id = request.POST['id']
            x = request.POST['x']
            qty = request.POST['qty']
    
            print(id)
    
            if x== 'add':  
                print("add")
                qty=int(qty)
                qty+=1
                print(qty)
                Cart.objects.filter(id=id).update(qty=qty)
                return JsonResponse(
                            {'success':'add'},
                            safe = False
                        )
            if x == 'minus':
                print("minus")
                qty=int(qty)
                qty-=1   
                print(qty)
                Cart.objects.filter(id=id).update(qty=qty)
                return JsonResponse(
                            {'success':'minus'},
                            safe = False
                        )
        else:
            return redirect('login')

def order(request,cartid):
    if request.session.has_key('username'):
        if request.method == 'POST':
            name = request.POST['name']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            pincode = request.POST['pincode']
            phone = request.POST['phone']

            c= Cart.objects.get(id=cartid)
            Order.objects.create(name=name,address=address,city=city,state=state,pincode=pincode,Phone=phone,cartid=c)
            
            return redirect('userdisplay')
        else:
            c = Cart.objects.all()
            cartid = int(cartid)
            user = User.objects.get(username=request.session['username'])
            name = user.first_name 
            return render(request,'user/order.html',{'cartid':cartid,'cart':c,'name1':name,'name2':"logout"})
    else:
            return redirect('login')