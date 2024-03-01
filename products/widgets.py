from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

"""
Custom widget for file inputs that allows clearing the file with
customized labels and templates.
"""


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'products/custom_widget_templates/custom_clearable_file_input.html')
