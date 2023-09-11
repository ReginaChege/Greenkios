from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    order = models.IntegerField()
    status = models.CharField(max_length=10)
    date = models.DateField()
    method_payment = models.CharField(max_length=20)
    
    