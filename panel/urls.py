from django.urls import path
from .views import homePageView, categoriesPageView, brandsPageView, createProduct, createBrand, createCategory, \
    productDetailView, productsByBrandDetailView, productsByCategoryDetailView, deleteProductDetailView, \
    developersPageView, updateProduct, detailsPageView

urlpatterns = [
    path('', homePageView),
    path('brands', brandsPageView, name="brand"),
    path('categories', categoriesPageView, name="categories"),
    path('create-product', createProduct, name="create-product"),
    path('create-brand', createBrand, name="create-brand"),
    path('create-category', createCategory, name="create-category"),
    path('product-view/<str:id>', productDetailView, name="product-detail"),
    path('products/brand/<str:id>', productsByBrandDetailView, name="product-detail-brand"),
    path('products/category/<str:id>', productsByCategoryDetailView, name="product-detail-category"),
    path('product-delete/<str:id>', deleteProductDetailView, name="product-delete"),
    path('product-edit/<str:id>', updateProduct, name="product-edit"),
    path('developers/', developersPageView, name="developers"),
    path('project-details/', detailsPageView, name="project-details")
]
