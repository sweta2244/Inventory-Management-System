from django.contrib import admin
from .models import User, ProductType, Product, Purchase, Department, Vendor, Sales, Customer
# Register your models here.

admin.site.register(User)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Department)
admin.site.register(Vendor)
admin.site.register(Sales)
admin.site.register(Customer)
