from django.db import models


class ContactForm(models.Model):
    contact_name = models.CharField(max_length=70, null=False, blank=False)
    contact_email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=200, default='No subject')
    contact_message = models.TextField(
        max_length=500, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    contact_phone_number = models.CharField(
        max_length=15, blank=True, null=True)

    def __str__(self):
        return self.contact_email
