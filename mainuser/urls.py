from django.urls import include, path

from . import views

urlpatterns = [
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('logout',views.logout,name='logout'),
    path('display',views.display,name='display'),
    path('delete/<username>/',views.delete,name='delete'),
    path('update/<username>/',views.update,name='update'),
    path('product',views.product,name='product'),
    path('deleteproduct/<id>/',views.deleteproduct,name='deleteproduct'),
    path('updateproduct/<id>/',views.updateproduct,name='updateproduct'),
    path('additem',views.additem,name='additem'),
    path('orderdisplay',views.orderdisplay,name='orderdisplay'), 
]
