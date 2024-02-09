from django.http import HttpResponseRedirect
from .context import display_subscribe_form
from django.contrib import messages
from .models import Newsletter
from .forms import SubscribeForm


def new_subscriber(request):
    """ Adds a new email to the subscriber list"""

    if request.method == 'POST':
        form = SubscribeForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            if Newsletter.objects.filter(email=email).exists():
                messages.error(
                    request, f"{email} already exists. Please enter email again.")
            else:
                form.save()
                messages.success(
                    request, f"{email} has been successfully added.")
    else:
        form = SubscribeForm(None)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
