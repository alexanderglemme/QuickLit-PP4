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
    Model for the book that the user wants to advertise on QuickLit
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

    # Makes a string representation of the members, joins them and returns it to be displayed along with the ad.title
    def __str__(self):
        members_str = ', '.join([str(member) for member in self.members.all()])
        return f"Members: {members_str} - Ad: {self.ad.title}"


class StudyGroup(models.Model):
    group_name = models.CharField(max_length=255)
    group_admin = models.ManyToManyField(User, related_name='group_admin')
    members = models.ManyToManyField(User, related_name='study_groups')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    # Makes unique slug for the study group
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.group_name + "-" + str(self.created_at))

        return super().save(*args, **kwargs)


class ConversationMessage(models.Model):
    study_group = models.ForeignKey(StudyGroup, related_name='study_group_messages', on_delete=models.CASCADE, null=True)
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
