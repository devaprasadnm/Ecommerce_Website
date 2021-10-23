from django.urls import include, path

from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('',views.home,name='home'),
    path('product/<product_id>/',views.product,name='product'),
    path('cart',views.cart,name='cart'),
    path('userdisplay',views.userdisplay,name='userdisplay'),
    path('calc',views.calc,name='calc'),
    path('order/<cartid>/',views.order,name='order'),
    path('category/<cid>/',views.category,name='category'),
]
