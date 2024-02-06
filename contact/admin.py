from django.contrib import admin
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):

    list_display = ('contact_email', 'created_on')

    ordering = ('-created_on',)


admin.site.register(ContactForm, ContactFormAdmin)