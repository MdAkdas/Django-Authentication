from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate #add this
import requests

# Create your views here.


def index(request):
    return render(request,'accounts/index.html')

@login_required
def dashboard(request):
    url = 'https://api.thecatapi.com/v1/images/search'
    r = requests.get(url)
    rd = r.json()
    d = rd[0]
    
    context = {}
    context['url'] = d['url']
    return render(request,'accounts/dashboard.html', context)

def login_view(request):
    print("in sign in view")
    
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect('dashboard')
            else:
                print('User not found')
        else:
            # If there were errors, we render the form with these
            # errors
            context = {}
            context['form']=form
        return render(request,'registration/login.html',context)


def sign_up_view(request):
    print("why not here")
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    context['form']=form
    return render(request,'registration/sign_up.html',context)

def logout_view(request):
    logout(request)
    return redirect('home')