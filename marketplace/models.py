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


class Chat(models.Model):
    participants = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"Chat {self.pk}"


class DirectMessage(models.Model):
    chat = models.ForeignKey(Chat, null=True, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return f"Message {self.pk}"

    def get_absolute_url(self):
        return reverse('chat')

