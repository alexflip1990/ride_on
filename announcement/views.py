from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AnnouncementForm

from .models import AnnouncementPost


@login_required
def announcement_list(request):
    """ A view to ensure only authenticated users can access the list of announcements"""

    announcements = Announcement.objects.all()
    return render(request, 'announcement_list.html', {'announcements': announcements})


@login_required
def announcement_detail(request, pk):
    """ A view to ensure only authenticated users can access the details of announcements"""

    announcement = get_object_or_404(Post, pk=pk)
    return render(request, 'announcement_detail.html', {'announcement': announcement})


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
            return redirect('announcement_detail', pk=announcement.pk)
    else:
        form = AnnouncementForm()
    return render(request, 'announcement_form.html', {'form': form})
