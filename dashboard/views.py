from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Client, Team, Product, Orders
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib import admin
import webbrowser

@login_required
def index(request):
    orders = Orders.objects.all()
    order_count = Orders.objects.count()
    order_pending = Orders.objects.filter(is_completed='0').count()
    user_count = Client.objects.count()
    return render(request, 'index.html', {'user_count': user_count, 'order_count': order_count, 'order_pending': order_pending, 'orders': orders})  

@login_required
def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

@login_required
def favorites(request):
    products = Product.objects.all()
    return render(request, 'favorites.html', {'products': products})

@login_required
def inbox(request):
    return render(request, 'inbox.html')

@login_required
def orders(request):
    orders = Orders.objects.all()
    return render(request, 'orderlist.html', {'orders': orders})

@login_required
def stock(request): 
    products = Product.objects.all()
    return render(request, 'productstock.html', {'products': products})

@login_required
def pricing(request):
    return render(request, 'pricing.html')

@login_required
def calendar(request):
    return render(request, 'calendar.html')

@login_required
def todo(request):
    return render(request, 'to-do.html')

@login_required
def contact(request):
    clients = Client.objects.all()
    return render(request, 'contact.html', {'clients': clients})

@login_required
def invoice(request):
    return render(request, 'invoice.html')

@login_required
def ui(request):
    return render(request, 'ui.html')

@login_required
def team(request):
    teams = Team.objects.all()
    users = User.objects.all()
    return render(request, 'team.html', {'users': users})


@login_required
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

# def clientRegister(request):
    # name = email = gender = None
    # try:
    #     new_client = Client.objects.create(name=name, email=email, gender=gender)
    #     new_client.save()
    # except Exception as e:
    #     print(f"Error creating client: {e}")
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     gender = request.POST['gender']

    #     new_client = Client.objects.create(name, email, gender)
    #     new_client.save()
    #     return redirect('/dashboard/team')
    
    # return render(request, 'contact.html')

def clientRegister(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        Client.objects.create(name=name, email=email, gender=gender)
        return render(request, 'contact.html')
    return render(request, 'contact.html')


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
                validate_user = None
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
    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    return redirect('/dashboard/login')






# def addUser(request):
#     # return redirect('/admin/auth/user/')
#     return webbrowser.open_new_tab('127.0.0.1:8000/admin/auth/user/')
    


