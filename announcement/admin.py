from django.contrib import admin
from .models import AnnouncementPost


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',
                    'content', 'created_on',
                    'updated_on')

    ordering = ('-created_on',)


admin.site.register(AnnouncementPost, AnnouncementAdmin)
