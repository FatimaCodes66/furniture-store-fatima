from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .models import Contact  
from store.models import Blog

def updates_page(request):
    blogs = Blog.objects.all().order_by('-id') 
    return render(request, 'store/updates.html', {'blogs': blogs})

def index(request):
    categories = Category.objects.all() 
    return render(request, 'store/index.html', {'categories': categories})

def blog(request):
    blogs = Blog.objects.all().order_by('-created_at') 
    return render(request, 'store/blog.html', {'blogs': blogs}) 

def blog_entry(request, blog_id): 
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'store/blog_detail.html', {'blog': blog})  

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        if name and email and subject and phone and message:
            contact = Contact(
                name=name,
                email=email,
                subject=subject,
                phone=phone,
                message=message
            )
            contact.save()
            messages.success(request, "✅ Thanks for contacting us! We'll get back to you shortly.")
            return redirect('contact')
        else:
            messages.error(request, "⚠️ Please fill in all fields.")

    return render(request, 'store/contact.html')


def success(request):
    return render(request, 'success.html')

def gallery(request):
    galleries = Gallery.objects.all()  
    return render(request, 'store/gallery.html', {'galleries': galleries})


def cart_view(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.get_total_price() for item in cart_items)
        return render(request, 'store/cart.html', {
            'cart_items': cart_items,
            'total_price': total_price
        })
    else:
        return redirect('login')


