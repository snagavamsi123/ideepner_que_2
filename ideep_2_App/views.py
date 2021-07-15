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

    failed = Customer.objects.raw('''
    select *,SUM(c) as failed_count 
    FROM (select *, count(*) as c 
            FROM (select * 
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
        select *,count(order_id) as count
		from ((ideep_queries.ideep_2_app_customer as cust
		inner join ideep_queries.ideep_2_app_order as ord on cust.customer_no=ord.customer_no_id))
        group by customer_name;
        
        '''
    )
    return render(request,'order_count.html',{'values':values})
    