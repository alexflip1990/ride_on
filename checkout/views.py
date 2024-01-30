from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There are no items in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OeI4cJWhOQxjshHrEl1BOcAAjSAFe5XSTXb46ZcTpRr4u5RJ0xlK3VMW2MgoqqWDZOCJtP862wdRreLTVdD0xV5004egYTsuM',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)


