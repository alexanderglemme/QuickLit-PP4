from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class SalesAd(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sales_ad')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    item_image = CloudinaryField('image', default='placeholder')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sales_ad')
    city = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    sold = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
