from django.contrib import admin
from .models import Gallery, update, Category, Blog,Contact

# Register your models here
admin.site.register(Gallery)
admin.site.register(update)
admin.site.register(Category)
admin.site.register(Blog)
# admin.site.register(Profile)

admin.site.register(Contact)
