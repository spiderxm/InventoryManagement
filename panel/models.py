from django.core.validators import MinValueValidator
from django.db import models


class Brand(models.Model):
    """
    Model to store brands
    """
    brand_name = models.CharField(max_length=256)
    brand_image = models.ImageField(upload_to="brands/")

    def __str__(self):
        return self.brand_name


class Category(models.Model):
    """
    Model to store categories
    """
    category_name = models.CharField(max_length=256)
    category_image = models.ImageField(upload_to="categories/")

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """
    Model to store products
    """
    name = models.CharField(max_length=256)
    quantity = models.IntegerField(
        validators=[MinValueValidator(limit_value=0, message="Quantity cannot be less than 0")])
    description = models.TextField(max_length=2056)
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(decimal_places=1, max_digits=10)
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
