from ideep_2_App.views import signup
from django.contrib import admin
from .models import Customer,Order,Payment,Signup
# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Signup)

