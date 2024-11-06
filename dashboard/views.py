from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Team
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib import admin
import webbrowser

@login_required
def index(request):
    user_count = User.objects.count()
    return render(request, 'index.html', {'user_count': user_count})

def products(request):
    return render(request, 'products.html')

def favorites(request):
    return render(request, 'favorites.html')

def inbox(request):
    return render(request, 'inbox.html')

def orders(request):
    return render(request, 'orderlist.html')

def stock(request): 
    return render(request, 'productstock.html')

def pricing(request):
    return render(request, 'pricing.html')

def calendar(request):
    return render(request, 'calendar.html')

def todo(request):
    return render(request, 'to-do.html')

def contact(request):
    return render(request, 'contact.html')

def invoice(request):
    return render(request, 'invoice.html')

def ui(request):
    return render(request, 'ui.html')

def team(request):
    teams = Team.objects.all()
    users = User.objects.all()
    return render(request, 'team.html', {'users': users})


def table(request):
    return render(request, 'table.html')


def register(request):
    username = email = password = None
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        return redirect('/dashboard/team')
    
    return render(request, 'register.html')

def loginpage(request):
   
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        validate_user = authenticate(request, email=email, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('index.html')
        # else:
        #     return redirect() 
    return render(request, 'login.html')


def loginpage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        print("Attempting to authenticate user...")
        try:
            user = User.objects.get(email=email)
            print("User found:", user)
            if user.check_password(password):
                print("Password correct!")
                validate_user = user
            else:
                print("Password incorrect!")
                validate_user = User.objects.none() 
        except User.DoesNotExist:
            print("User not found!")
            validate_user = None

        print("Authentication result:", validate_user)

        if validate_user is not None:
            print("Login successful! Redirecting to index page...")
            login(request, validate_user)
            return redirect('/dashboard')
        else:
            print("Login failed!")
    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    return redirect('/dashboard/login')






# def addUser(request):
#     # return redirect('/admin/auth/user/')
#     return webbrowser.open_new_tab('127.0.0.1:8000/admin/auth/user/')
    


