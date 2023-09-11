from django.shortcuts import render, redirect
from .forms import ProductUploadForm
from .models import Product

def upload_product(request):
    if request.method == "POST":
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductUploadForm()
    return render(request, 'inventory/product-upload.html', {'form': form})


def products_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product-list.html', {'products': products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'inventory/product-detail.html', {'product': product})


def add_to_cart(request):
    cartitems = []
    return render(request, 'inventory/add_to_cart.html', {'cartitems': cartitems})


def edit_product_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail_view', id=product.id)
    else:
        form = ProductUploadForm(instance=product)
    return render(request, 'inventory/edit_product.html', {'form': form})