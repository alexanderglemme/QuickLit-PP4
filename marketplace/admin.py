from django.contrib import admin
from .models import Category, SalesAd, DirectMessage, Chat


admin.site.register(Category)
admin.site.register(SalesAd)
admin.site.register(DirectMessage)
admin.site.register(Chat)
