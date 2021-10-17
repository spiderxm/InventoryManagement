from django.urls import path
from .views import homePageView, categoriesPageView, brandsPageView, createProduct, createBrand, createCategory

urlpatterns = [
    path('', homePageView),
    path('brands', brandsPageView, name="brand"),
    path('categories', categoriesPageView, name="categories"),
    path('create-product', createProduct, name="create-product"),
    path('create-brand', createBrand, name="create-brand"),
    path('create-category', createCategory, name="create-category")
]
