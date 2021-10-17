from django.shortcuts import render
from .models import Product, Category, Brand
from .forms import ProductForm, BrandForm, CategoryForm
from django.shortcuts import redirect


def homePageView(request):
    """
    Home Page View
    """
    products = Product.objects.all()

    return render(request=request, template_name="home.html", context={
        "products": products
    })


def categoriesPageView(request):
    """
    Home Page View
    """
    category = Category.objects.all()

    return render(request=request, template_name="categories.html", context={
        "categories": category
    })


def brandsPageView(request):
    """
    Home Page View
    """
    brands = Brand.objects.all()

    return render(request=request, template_name="brands.html", context={
        "brands": brands
    })


def createProduct(request):
    """
    Create Product View
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        product = Product.objects.create(
            name=form.data['name'],
            description=form.data['description'],
            image=request.FILES['image'],
            quantity=form.data['quantity'],
            brand_id=form.data['brand'],
            category_id=form.data['category'],
            price=form.data['price']
        )
        product.save()
        return redirect("/")
    else:
        form = ProductForm()
    return render(request, 'create-product.html', {'form': form})


def createBrand(request):
    """
    Create Brand View
    """
    if request.method == 'POST':
        form = BrandForm(request.POST)
        brand = Brand.objects.create(
            brand_name=form.data['brand_name'],
            brand_image=request.FILES['brand_image'],
        )
        brand.save()
        return redirect("/")
    else:
        form = BrandForm()
    return render(request, 'create-brand.html', {'form': form})


def createCategory(request):
    """
    Create Category View
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        category = Category.objects.create(
            category_name=form.data['category_name'],
            category_image=request.FILES['category_image'],
        )
        category.save()
        return redirect("/")
    else:
        form = CategoryForm()
    return render(request, 'create-category.html', {'form': form})
