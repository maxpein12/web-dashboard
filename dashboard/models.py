from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    


class Client(models.Model):
    username = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    email = models.EmailField()
    profile_pic = models.CharField(max_length=100, default='')
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.name} {self.email} {self.gender}'
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    piece = models.IntegerField()
    # image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    

class Orders(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    type = models.CharField(max_length=100)
    quantity = models.IntegerField(8)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message