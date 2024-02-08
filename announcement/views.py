from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AnnouncementForm

from .models import AnnouncementPost


@login_required
def announcement_list(request):
    """ A view to ensure only authenticated users can access the list of announcements"""

    announcements = AnnouncementPost.objects.all()
    return render(request, 'announcement/announcement_list.html', {'announcements': announcements})


@login_required
def announcement_detail(request, pk):
    """ A view to ensure only authenticated users can access the details of announcements"""

    announcement = get_object_or_404(AnnouncementPost, pk=pk)
    return render(request, 'announcement/announcement_detail.html', {'announcement': announcement})


@login_required
def announcement_create(request):
    """ Add an announcement to the page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only staff members can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.author = request.user
            announcement.save()
            return redirect(reverse('announcement_detail', args=[announcement.pk]))
    else:
        form = AnnouncementForm()

    template = 'announcement/announcement_form.html'
    context = {
        'form': form
    }
    return render(request, template, context)


@login_required
def announcement_edit(request, pk):
    """ Edit an announcement on the page """
    announcement = get_object_or_404(AnnouncementPost, pk=pk)
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only staff members can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.save()
            return redirect(reverse('announcement_detail', args=[announcement.pk]))
    else:
        form = AnnouncementForm(instance=announcement)

    template = 'announcement/announcement_form.html'
    context = {
        'form': form
    }
    return render(request, template, context)


@login_required
def announcement_delete(request, pk):
    """ Delete an announcement on the page """
    announcement = get_object_or_404(AnnouncementPost, pk=pk)
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only staff members can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        announcement.delete()
        return HttpResponseRedirect(reverse('announcement_list'))
    else:
        # Handle GET request, render the delete confirmation page
        return render(request, 'announcement/announcement_delete.html', {'announcement': announcement})
