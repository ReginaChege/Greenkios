from django.db import models

# Create your models here.
class Deliver(models.Model):
    date = models.DateField()
    delivery_cost = models.DecimalField(max_digits=10,decimal_places=2)
    order_status = models.CharField(max_length=20)
    delivery_method = models.CharField(max_length=10)
    delivery_person = models.CharField(max_length=25)
    def __str__(self):
        return self.delivery_person
       