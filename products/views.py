from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, SubCategory


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    subcategories = None
    paintings = None

    if request.GET:
        # Handles the category filtering
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Handles the subcategory filtering
        if 'subcategory' in request.GET:
            subcategories = request.GET['subcategory'].split(',')
            products = products.filter(subcategory__name__in=subcategories)
            subcategories = SubCategory.objects.filter(name__in=subcategories)

        # Handles search query
        if 'q' in request.GET:
            Query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) | 
                Q(description__icontains=query) |
                Q(category__name__icontains=query) |
                Q(subcategory__name__icontains=query)
                )

            products = products.filter(queries)

    subcategories = SubCategory.objects.all()

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_subcategories': subcategories,
        'subcategories': subcategories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
