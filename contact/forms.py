from django import forms
from .models import ContactForm


class CustomerContactForm(forms.ModelForm):

    class Meta:
        model = ContactForm
        fields = ('contact_name', 'contact_email', 'contact_message',
                  'contact_phone_number')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'contact_name': 'Name',
            'contact_email': 'Email Address',
            'contact_message': 'Your Message',
            'contact_phone_number': 'Phone Number'
        }

        self.fields['contact_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
