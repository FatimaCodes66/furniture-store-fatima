from django.shortcuts import render
from .models import Product, Category

def home_view(request):
    products = Product.objects.all()[:5]  # Show 5 latest products
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories
    })