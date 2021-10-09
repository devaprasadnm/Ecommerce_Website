from django.urls import include, path

from . import views

urlpatterns = [
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('logout',views.logout,name='logout'),
    path('display',views.display,name='display')
    
]
