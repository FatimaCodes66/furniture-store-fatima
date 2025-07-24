from django.urls import path
from . import views
from .views import cart_view  

urlpatterns = [
    path('', views.index, name='index'),  # Homepage
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>/', views.blog_entry, name='blog_entry'),  
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('success/', views.success, name='success'),
    path('updates/', views.updates_page, name='updates'),
    path('cart/', cart_view, name='cart'), 
]
