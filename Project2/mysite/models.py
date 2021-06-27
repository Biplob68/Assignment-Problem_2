from django.db import models
from django.conf import settings

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=111, default="")
    message= models.CharField(max_length=500)

    def __str__(self):
        return self.name + " - " + self.email
