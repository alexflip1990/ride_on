from django.contrib import admin
from .models import Product, Category, SubCategory


"""
Customizes the display and ordering of products in
Django admin.
"""


class ProductAdmin(admin.ModelAdmin):
    # Specifies fields to display in the product list view
    list_display = (
        'category',
        'name',
        'sku',
        'year',
        'size',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'category'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
