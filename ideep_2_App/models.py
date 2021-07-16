from django.db import models
from django.utils import timezone

class Customer(models.Model):
    customer_no = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=25)
    City = models.CharField(max_length=25)
    State = models.CharField(max_length=25)
    def __str__(self):
        return str(self.customer_name)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(timezone.now())
    order_amount = models.FloatField()
    customer_no = models.ForeignKey(Customer,on_delete=models.CASCADE,default=0)
    def __str__(self):
        return str('order ID' + str(self.order_id))

status_chioces = (('failed','FAILED'),('paid','PAID'))
class Payment(models.Model):
    payment_id =models.AutoField(primary_key=True)
    status = models.CharField(max_length=10,choices=status_chioces)
    order_id= models.ForeignKey(Order,on_delete=models.CASCADE,default=0)

    def __str__(self):
        return str(self.payment_id)
