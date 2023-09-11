from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=8)
    identification = models.AutoField(primary_key=True)
    location = models.CharField(max_length=10)
    contacts = models.CharField(max_length=20)
