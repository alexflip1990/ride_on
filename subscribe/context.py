from .forms import SubscribeForm


def display_subscribe_form(request):
    """ Displays the subscribe newsletter form on each page """

    subscribe_form = SubscribeForm()
    context = {
        'subscribe_form': subscribe_form,
    }

    return context
