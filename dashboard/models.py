from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
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