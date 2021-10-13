from django.urls import include, path

from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('',views.home,name='home'),
    path('userdisplay',views.userdisplay,name='userdisplay')
]
