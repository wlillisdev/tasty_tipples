from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    """
    Class to display contact model in admin.
    """
    list_display = ('name', 'subject', 'email', 'message',)


admin.site.register(ContactUs, ContactUsAdmin)
