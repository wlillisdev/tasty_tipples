from django.db import models

# Create your models here.


class ContactUs(models.Model):
    """
    Site user can submit a message via a form
    """
    class Meta:
        verbose_name_plural = 'Contact Us'
    name = models.CharField(max_length=60)
    subject = models.CharField(max_length=60)
    email = models.EmailField(max_length=250, null=False, blank=False)
    message = models.TextField(max_length=1200)

    def __str__(self):
        return str(self.name)
