from django.contrib import admin

# Register your models here.
from .models import product 


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','description','price','summary')

admin.site.register(product,ProductAdmin)
