from django.shortcuts import render, redirect
from .forms import CustomerContactForm
from profiles.models import UserProfile

from django.contrib import messages


def delivery(request):
    """ A view to return the delivery page"""

    return render(request, 'contact/about/delivery.html')


def privacy(request):
    """ A view to return the privacy page"""

    return render(request, 'contact/about/privacy.html')


def t_and_c(request):
    """ A view to return the t and c page"""

    return render(request, 'contact/about/t_and_c.html')


def contact(request):

    if request.method == 'POST':
        contact_form = CustomerContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Message sent successfully.')
            return render(request, 'contact/contact_success.html')
        else:
            messages.error(request, 'An error occured sending your message. \
            Please ensure all fields are valid.')
            return redirect('contact')

    else:
        if request.user.is_authenticated:
            try:
                user = UserProfile.objects.get(user=request.user)
                contact_form = CustomerContactForm(initial={
                    'contact_name': user.default_full_name,
                    'contact_email': user.user.email,
                    'contact_phone_number': user.default_phone_number,
                })
            except UserProfile.DoesNotExist:
                contact_form = CustomerContactForm()
        else:
            contact_form = CustomerContactForm()

    template = 'contact/contact.html'
    context = {
        'form': contact_form,
    }

    return render(request, template, context)
