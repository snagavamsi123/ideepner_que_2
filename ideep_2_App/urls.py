from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('failed',views.failed,name='failed'),
    path('total_amount',views.total_amount,name='total_amount'),
    path('order_count',views.order_count,name='order_count'),
    path('add_new',views.add,name='add'),
]

