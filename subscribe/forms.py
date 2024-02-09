from django import forms
from .models import Newsletter


class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        """
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'
        self.fields['email'].widget.attrs['class'] = 'border-black'
        self.fields['email'].widget.attrs['id'] = 'email_subscribe'
        self.fields['email'].label = False
