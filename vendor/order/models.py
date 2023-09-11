from django.db import models
from payment.models import Payment
from customer.models import Customer
from basket.models import Basket
from shippment.models import Shipment
# Create your models here.
class Order(models.Model):
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    basket=models.ForeignKey(Basket,on_delete=models.CASCADE)
    shipment=models.ForeignKey(Shipment,on_delete=models.CASCADE)
    payment= models.OneToOneField(Payment,on_delete=models.PROTECT,null=True,related_name='order_payments')
    quantity = models.IntegerField()
    date = models.DateTimeField()
    total = models.DecimalField(max_digits=10,decimal_places=2)
    name = models.CharField(max_length=20)
    
def __str__(self):
        return self.name 