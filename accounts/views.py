from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
import requests

# view for home page
# home page will contain login and sign up option
def index(request):
    return render(request,'accounts/index.html')


# to view dashboard with a cat,
# user must login
#using decorator to ensure this
@login_required
def dashboard(request):

    # using an api to fetch a cat
    url = 'https://api.thecatapi.com/v1/images/search'
    r = requests.get(url)
    rd = r.json()
    d = rd[0]
    context = {}
    context['url'] = d['url']
    return render(request,'accounts/dashboard.html', context)


def login_view(request):

    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        print("authenticating....")
        if form.is_valid(): # will ensure the username and password validation
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect('dashboard') # upon sign up, redirect to dashbaord
            else:
                print('User not found')
        else:
            # If there were errors, we render the form with these
            # errors
            context = {}
            context['form']=form
        return render(request,'registration/login.html',context)


def sign_up_view(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():# will ensure the username and password validation
            user = form.save()
            login(request,user)
            return redirect('dashboard') # upon sign up, redirect to dashbaord
    context['form']=form
    return render(request,'registration/sign_up.html',context)


def logout_view(request):
    logout(request) # will logout current user
    return redirect('home')