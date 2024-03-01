from django.http import HttpResponseRedirect
from .context import display_subscribe_form
from django.contrib import messages
from .models import Newsletter
from .forms import SubscribeForm


def new_subscriber(request):
    """ Adds a new email to the subscriber list"""
    # If the request method is POST, process the form data
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if the email already exists in the database
            if Newsletter.objects.filter(email=email).exists():
                messages.error(
                    request, f"{email} already exists. \
                        Please enter email again.")
            else:
                # Save the form data and display success message
                form.save()
                messages.success(
                    request, f"{email} has been successfully added.")
    # If the request method is not POST, display the empty form
    else:
        form = SubscribeForm(None)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
