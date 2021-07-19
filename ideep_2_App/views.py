from django.shortcuts import render
from .models import Customer,Order,Payment
from .forms import CustomerForm, Loginform,OrderForm,PaymentForm,Signupform

def home(request):
    values1=Customer.objects.all()
    values2 = Order.objects.all()
    values3=Payment.objects.all()
    return render(request,'home.html',{'values1':values1,'values2':values2,'values3':values3})

def failed(request):
    failed = Customer.objects.raw('''
    select *,SUM(c) as failed_count 
    FROM (select *, count(*) as c 
            FROM (  select * 
                    FROM ((ideep_queries.ideep_2_app_customer as cust 
                    INNER JOIN ideep_queries.ideep_2_app_order AS ord 
                        ON cust.customer_no=ord.customer_no_id) 
                    INNER JOIN ideep_queries.ideep_2_app_payment AS pay 
                        ON ord.order_id=pay.order_id_id)) AS outer_table 
                GROUP BY order_id_id,status having (status)='failed') as table2   
                GROUP BY customer_name ''')

           
    return render(request,'Failed.html',{'values':failed})

def total_amount(request): 

    values = Customer.objects.raw(
        '''
        select *,SUM(order_amount) as state_amount
		from (ideep_queries.ideep_2_app_customer as cust
		inner join ideep_queries.ideep_2_app_order as ord on cust.customer_no=ord.customer_no_id)
        group by State;
        
        '''
    )
    return render(request,'total_amount.html',{'values':values})
    

def order_count(request):

    values = Customer.objects.raw(
        '''
        select * ,ROW_NUMBER() over (partition by customer_no_id order by order_id) as order_count
        from (ideep_queries.ideep_2_app_order as ord
		inner join ideep_queries.ideep_2_app_customer as cust on cust.customer_no=ord.customer_no_id)
        order by order_id;
        
        '''
    )
    return render(request,'order_count.html',{'values':values})


def add_order(request):
    if request.method=='POST':
        form1=OrderForm(request.POST)
        if form1.is_valid():
            form1.save()
            message = 'Successfully Saved'
            return render(request,'add_order.html',{'form':form1,'message':message}) 
        else:
            message = 'Validation Failed'
            return render(request,'add_order.html',{'form':form1,'message':message}) 

    form1 = OrderForm
    return render(request,'add_order.html',{'form':form1})

def add_customer(request):
    if request.method=='POST':
        form2=CustomerForm(request.POST)
        name = request.POST['customer_name']
        city_name = request.POST['City']
        form = Customer.objects.all()
        for data in form:
            if data.customer_name==name and data.City==city_name:
                message = 'User Already exist Failed'
                return render(request,'add_customer.html',{'form':form2,'message':message}) 
        if form2.is_valid():
            form2.save()
            message = 'Successfully Saved'
            return render(request,'add_customer.html',{'form':form2,'message':message}) 
        else:
            message = 'Validation Failed'
            return render(request,'add_customer.html',{'form':form2,'message':message}) 
    form2=CustomerForm
    return render(request,'add_customer.html',{'form':form2})

def payment(request):
    if request.method=='POST':
        form3=PaymentForm(request.POST)
        if form3.is_valid():
            form3.save()
            message = 'Successfully Saved'
            return render(request,'add_payment.html',{'form':form3,'message':message}) 
        else:
            message = 'Validation Failed'
            return render(request,'add_payment.html',{'form':form3,'message':message}) 
    form3=PaymentForm
    return render(request,'add_payment.html',{'form':form3})


def signup(request):
    signupform = Signupform
    return render(request,'signup.html',{'signupform' : signupform})

def login(request):
    loginform = Loginform
    return render(request,'login.html',{'loginform':loginform})
    