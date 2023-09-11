from django.db import models

# Create your models here.
class Shipment(models.Model):
    name_origin=models.CharField(max_length=10)
    weight=models.DecimalField(max_digits=5,decimal_places=2)
    destination=models.CharField(max_length=30)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
      return self.name_origin
 