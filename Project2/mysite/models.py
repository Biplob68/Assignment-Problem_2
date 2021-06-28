from django.db import models
from django.conf import settings

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=15)

class Reg(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)



class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=111, default="")
    message= models.CharField(max_length=500)

    def __str__(self):
        return self.name + " - " + self.email
