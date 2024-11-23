from django.shortcuts import redirect, render, get_object_or_404
from .models import Client, Team, Product, Orders, Messages
from .models import Users
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import datetime
from django.contrib.auth import *
import hashlib
from dashboard.auth_backend import SHA2Backend




now = datetime.datetime.now()

def index(request):
    orders = Orders.objects.all().order_by('-date')
    products = Product.objects.all()
    order_count = Orders.objects.count()

    orders_january = Orders.objects.filter(date__month='1', date__year = now.year).aggregate(total=Sum('price'))
    orders_february = Orders.objects.filter(date__month='2', date__year=now.year).aggregate(total=Sum('price'))
    orders_march = Orders.objects.filter(date__month='3', date__year=now.year).aggregate(total=Sum('price'))
    orders_april = Orders.objects.filter(date__month='4', date__year=now.year).aggregate(total=Sum('price'))
    orders_may = Orders.objects.filter(date__month='5', date__year=now.year).aggregate(total=Sum('price'))
    orders_june = Orders.objects.filter(date__month='6', date__year=now.year).aggregate(total=Sum('price'))
    orders_july = Orders.objects.filter(date__month='7', date__year=now.year).aggregate(total=Sum('price'))
    orders_august = Orders.objects.filter(date__month='8', date__year=now.year).aggregate(total=Sum('price'))
    orders_september = Orders.objects.filter(date__month='9', date__year=now.year).aggregate(total=Sum('price'))
    orders_october = Orders.objects.filter(date__month='10', date__year=now.year).aggregate(total=Sum('price'))
    orders_november = Orders.objects.filter(date__month='11', date__year=now.year).aggregate(total=Sum('price'))
    orders_december = Orders.objects.filter(date__month='12', date__year=now.year).aggregate(total=Sum('price'))

    order_pending = Orders.objects.filter(is_completed='0', date__year=now.year).count()
    order_delivered = Orders.objects.filter(is_completed='1', date__year=now.year).count()
    total_sales = Orders.objects.filter(is_completed='1', date__year=now.year).aggregate(total=Sum('price'))

    user_count = Client.objects.count()
    return render(request, 'index.html', {'user_count': user_count, 'order_count': order_count, 'order_pending': order_pending, 'orders': orders, 'orders_november': orders_november, 'orders_january': orders_january, 'orders_february': orders_february, 'orders_march': orders_march, 'orders_april': orders_april, 'orders_may': orders_may, 'orders_june': orders_june, 'orders_july': orders_july, 'orders_august': orders_august, 'orders_september': orders_september, 'orders_october': orders_october, 'orders_december': orders_december, 'products': products, 'total_sales': total_sales, 'order_delivered': order_delivered})  


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def favorites(request):
    products = Product.objects.all()
    return render(request, 'favorites.html', {'products': products})


def inbox(request):
    messages = Messages.objects.all().order_by('-timestamp')
    
    return render(request, 'inbox.html', {'messages': messages})


def orders(request):
    orders = Orders.objects.all().order_by('-date')
    if request.method == 'POST':
        fromdate = request.POST.get('fromdate', '')
        todate = request.POST.get('todate', '')
        name = request.POST.get('name', '')
        status = request.POST.get('status', '')

        filters = {}

        if fromdate and todate:
            filters['date__range'] = [fromdate, todate]

        if name:
            filters['name'] = name

        if status and status != 'all':
            if status == 'completed':
                status = True
            elif status == 'processing':
                status = False
            
            filters['is_completed'] = status

        searchresult = Orders.objects.filter(**filters).order_by('-date')
        return render(request, 'orderlist.html', {'orders': searchresult})
    elif request.method == 'GET':
        orders = Orders.objects.all().order_by('-date')
        return render(request, 'orderlist.html', {'orders': orders})
    else:
        orders = Orders.objects.all().order_by('-date')
        return render(request, 'orderlist.html', {'orders': orders})





def stock(request): 
    products = Product.objects.all()
    return render(request, 'productstock.html', {'products': products})


def pricing(request):
    return render(request, 'pricing.html')


def calendar(request):
    return render(request, 'calendar.html')


def todo(request):
    return render(request, 'to-do.html')


def contact(request):
    users = Users.objects.all()
    print(users)  # Print the users variable
    return render(request, 'contact.html', {'users': users})
   


def invoice(request):
    orders = Orders.objects.all().order_by('-date')
    
    return render(request, 'invoice.html', {'orders': orders})

def ui(request):    
    return render(request, 'ui.html')


def team(request):
    teams = Team.objects.all()
    users = User.objects.all()
    return render(request, 'team.html', {'users': users})



def table(request):
    return render(request, 'table.html')



# def register(request):
    # username = email = password = None
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     new_user = User.objects.create_user(username, email, password)
    #     new_user.save()
    #     return redirect('/dashboard/team')
    
    # return render(request, 'register.html')
    


def clientRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        new_client = Client.objects.create(name=name, age=age, username=username , email=email, gender=gender)
        new_client.save()
        return redirect('contact')
    return render(request, 'register.html')


import hashlib

def loginpage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = Users.objects.get(email=email)
            salt = user.salt  # assuming you have a 'salt' field in your Users model
            hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
            if hashed_password == user.password and user.type == 0:
                # Login the user
                login(request, user)
                print("Login successful! Redirecting to index page...")
                return redirect('/dashboard')
            else:
                print("Password is incorrect")
        except Users.DoesNotExist:
            print("Email does not exist")
        error_msg = 'Invalid username or password'
        return render(request, 'login.html', {'error': error_msg})
    return render(request, 'login.html')


def logoutpage(request):
    logout(request)
    return redirect('/dashboard/login')




def  test(request, pkuser):
    user = get_object_or_404(Users, pk=pkuser)
    
    return render(request, 'test.html', {'user': user})