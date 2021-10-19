from django.shortcuts import render
from .models import Product, Category, Brand, Developer
from .forms import ProductForm, BrandForm, CategoryForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


def detailsPageView(request):
    """
    Details Page View
    """
    return render(request=request, template_name="details.html")


def homePageView(request):
    """
    Home Page View
    """
    products = Product.objects.all()
    searchKey = request.GET.get('search', None)
    if searchKey:
        products = products.filter(name__contains=searchKey)
    return render(request=request, template_name="home.html", context={
        "products": products,
        "searchform": True
    })


def categoriesPageView(request):
    """
    Categories Page View
    """
    category = Category.objects.all()
    searchKey = request.GET.get('search', None)
    if searchKey:
        category = category.filter(category_name__contains=searchKey)
    return render(request=request, template_name="categories.html", context={
        "categories": category,
        "searchform": True
    })


def brandsPageView(request):
    """
    Brand Page View
    """
    brands = Brand.objects.all()
    searchKey = request.GET.get('search', None)
    if searchKey:
        brands = brands.filter(brand_name__contains=searchKey)
    return render(request=request, template_name="brands.html", context={
        "brands": brands,
        "searchform": True
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


def productDetailView(request, id):
    """
    Product Detail View
    """
    product = get_object_or_404(Product, pk=id)
    return render(request, "product-details.html", {"product": product})


def deleteProductDetailView(request, id):
    """
    Product Delete View
    """
    if request.method == "GET":
        product = get_object_or_404(Product, pk=id)
        return render(request, "product-delete.html", {"product": product})

    if request.method == "POST":
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return redirect("/")


def productsByBrandDetailView(request, id):
    """
    Product Detail View by brand
    """
    brand = get_object_or_404(Brand, pk=id)
    products = Product.objects.all().filter(brand=brand)
    return render(request, "brand-products.html", {"products": products})


def productsByCategoryDetailView(request, id):
    """
    Product Detail View by category
    """
    category = get_object_or_404(Category, pk=id)
    products = Product.objects.all().filter(category=category)
    return render(request, "category-products.html", {"products": products})


def developersPageView(request):
    """
    Developers Page View
    """
    developers = Developer.objects.all()

    return render(request=request, template_name="developers.html", context={
        "developers": developers
    })


def updateProduct(request, id):
    """
    Update Product View
    """
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        product.name = form.data['name']
        product.description = form.data['description']
        product.quantity = form.data['quantity']
        product.brand_id = form.data['brand']
        product.category_id = form.data['category']
        product.price = form.data['price']
        if 'image' in request.FILES:
            print(23)
            product.image = request.FILES['image']
        product.save()
        return redirect("/")
    else:
        form = ProductForm(instance=product)
    return render(request, 'create-product.html', {'form': form})
