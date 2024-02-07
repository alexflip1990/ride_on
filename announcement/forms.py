from django import forms
from .models import AnnouncementPost


class AnnouncementForm(forms.ModelForm):

    class Meta:
        model = AnnouncementPost
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'content': 'Content',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['title'].widget.attrs['class'] = 'border-black'
        self.fields['content'].widget.attrs['class'] = 'border-black'
        self.fields['title'].label = False
        self.fields['content'].label = False
           
