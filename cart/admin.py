from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','total_quantity', 'total_price']

@admin.register(CardProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ['product','quantity','price']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['first_name','id']
	list_display_links = ['first_name' ]
	list_filter = ['payed','state','payment_method']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
	list_display = ['first_name','id']
	list_display_links = ['first_name' ]
	list_filter = ['payed','state','payment_method']