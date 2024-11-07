from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('favorites/', views.favorites, name='favorites'),
    path('inbox/', views.inbox, name='inbox'),
    path('orders/', views.orders, name='orders'),
    path('stock/', views.stock, name='stock'),
    path('pricing/', views.pricing, name='pricing'),
    path('ui/', views.ui, name='ui'),
    path('team/', views.team, name='team'),
    path('table/', views.table, name='table'),
    path('invoice/', views.invoice, name='invoice'),
    path('contact/', views.contact, name='contact'),
    path('calendar/', views.calendar, name='calendar'),
    path('todo/', views.todo, name='todo'),
    path('stock/', views.stock, name='stock'),
    path('orders/', views.orders, name='orders'),
    path('login/', views.loginpage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutpage, name='logout'),

]