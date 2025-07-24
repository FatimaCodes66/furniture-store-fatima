from django.db import models
from django.contrib.auth.models import User

class Gallery(models.Model):
    img = models.ImageField(upload_to='pics')

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"

    def __str__(self):
        return f"Gallery Image {self.id}"


class update(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=50)
    desc = models.TextField()
    writter = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        verbose_name = "Update"
        verbose_name_plural = "Updates"

    def __str__(self):
        return self.title


class Category(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='store_cart_items')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.title}'

    def get_total_price(self):
        return self.product.price * self.quantity


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
