from django import forms
from .models import Order,Payment,Customer
from  django.forms import ModelForm
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
    
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
class PaymentForm(ModelForm):
    class Meta:
        model=Payment
        fields= '__all__'