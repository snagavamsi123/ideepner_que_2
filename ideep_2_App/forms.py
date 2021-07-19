from django.db.models import fields
from django import forms
from .models import Order,Payment,Customer,Signup
from  django.forms import ModelForm
from django.forms import widgets
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
    
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets={
            'order_date':widgets.SelectDateWidget(),
        }
class PaymentForm(ModelForm):
    class Meta:
        model=Payment
        fields= '__all__'

class Signupform(ModelForm):
    class Meta:
        model=Signup
        fields = '__all__'
        widgets = {
            'password' :widgets.PasswordInput(),
        }
class Loginform(ModelForm):
    class Meta:
        model=Signup
        fields = ('username','password')
        widgets = {
            'password' :widgets.PasswordInput(),
        }