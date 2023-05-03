from django.contrib import admin
from .models import Category, SalesAd, Conversation, ConversationMessage


admin.site.register(Category)
admin.site.register(SalesAd)
admin.site.register(Conversation)
admin.site.register(ConversationMessage)
