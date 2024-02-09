from django.contrib import admin
from .models import Newsletter


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_on')

    ordering = ('-created_on',)


admin.site.register(Newsletter, SubscribeAdmin)
