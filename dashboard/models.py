from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    


