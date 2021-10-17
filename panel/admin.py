from django.contrib import admin
from .models import Product, Brand, Category

admin.site.register([
    Product,
    Brand,
    Category
])
