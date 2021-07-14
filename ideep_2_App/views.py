from django.shortcuts import render
from .models import Customer,Order,Payment




def home(request):
    values1=Customer.objects.all()
    values2 = Order.objects.all()
    values3=Payment.objects.all()
    return render(request,'home.html',{'values1':values1,'values2':values2,'values3':values3})

def failed(request):
    values1=Customer.objects.all()
    values2 = Order.objects.all()
    values3=Payment.objects.all()

    failed = Payment.objects.filter(status='failed')
           
    return render(request,'Failed.html',{'values':failed})

def total_amount(request): 
    values = Order.objects.all()
    return render(request,'total_amount.html',{'values':values})
    

def order_count(request):
    values1=Customer.objects.all()
    values2 = Order.objects.all()
    values3=Payment.objects.all()
    return render(request,'order_count.html',{'values1':values1,'values2':values2,'values3':values3})
    