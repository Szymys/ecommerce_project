from django.contrib import admin

from . models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

# AUTOMATYCZNIE DODAJE SLUG JAK WPROWADZAM NAME
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}


