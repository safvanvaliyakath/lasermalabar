from django.contrib import admin
from . models import *
# Register your models here.

class categories(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,categories)

class product(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
admin.site.register(products,product)