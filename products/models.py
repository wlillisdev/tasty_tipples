from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    """
    Product Review Model
    """
    rating_selection = (
        (5, '5 stars'),
        (4, '4 stars'),
        (3, '3 stars'),
        (2, '2 stars'),
        (1, '1 stars'),
    )

    product = models.ForeignKey(Product,
                                related_name='reviews',
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL)
    user = models.ForeignKey(User,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    content = models.TextField(default='', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=rating_selection,
                                 default=4,
                                 null=True,
                                 blank=True)

    class Meta:
        """
        Defines review rating values.
        """
        ordering = ['-date_added']

    def __str__(self):
        return self.title
