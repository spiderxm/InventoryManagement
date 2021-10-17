from django import forms
from .models import Product, Category, Brand


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['updated_at', 'created_at', 'id']


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
