from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # home page with login and signup option
    path('',views.index,name="home"),   

    #authentication required to view the dashboard with a cat
    path('dashboard/',views.dashboard,name="dashboard"),

    # login, signup and logout urls connecting to custom view
    # not using django built in auth system 'django.contrib.auth.views'
    path('accounts/login/',views.login_view,name="login"),
    path('accounts/sign_up/',views.sign_up_view,name="sign-up"),
    path('accounts/logout/',views.logout_view,name="logout")

]