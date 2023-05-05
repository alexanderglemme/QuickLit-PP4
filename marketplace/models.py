from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField

# Just read a thread on stackoverflow that says this is more reusable
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class SalesAd(models.Model):
    """
    Model for the post or item that the user wants to advertise
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sales_ad')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    item_image = CloudinaryField('image', default='placeholder')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sales_ad')
    city = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=timezone.now)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    sold = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    # Makes unique slug using title and time when created
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" + str(self.created_on))

        return super().save(*args, **kwargs)


class Conversation(models.Model):
    ad = models.ForeignKey(SalesAd, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-updated_at']


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)

