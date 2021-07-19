from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('failed',views.failed,name='failed'),
    path('total_amount',views.total_amount,name='total_amount'),
    path('order_count',views.order_count,name='order_count'),
    path('add_customer',views.add_customer,name='add_customer'),
    path('add_order',views.add_order,name='add_order'),
    path('payment',views.payment,name='payment'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),

]

