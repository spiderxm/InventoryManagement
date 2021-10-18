from django.contrib import admin
from .models import Product, Brand, Category, Developer

admin.site.register([
    Product,
    Brand,
    Category,
    Developer
])
