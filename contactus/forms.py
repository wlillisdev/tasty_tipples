from django.forms import ModelForm
from .models import ContactUs


class ContactForm(ModelForm):
    """
    Contact form to be displayed on Contact Us page
    """

    class Meta:
        """
        Extracts fields from model.
        """
        model = ContactUs
        fields = [
            'name',
            'subject',
            'email',
            'message',
        ]
