from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),   
    path('dashboard/',views.dashboard,name="dashboard"),   
    path('accounts/login/',views.login_view,name="login"),
    path('accounts/sign_up/',views.sign_up_view,name="sign-up"),
    path('accounts/logout/',views.logout_view,name="logout")

]