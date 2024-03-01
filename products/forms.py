from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category

"""
Defines a form for adding or editing products in Django admin.
"""


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    # Defines an image field with custom widget for the product form
    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Retrieves all categories and assigns them as choices
        # for the 'category' field
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
