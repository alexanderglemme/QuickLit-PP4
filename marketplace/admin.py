from django.contrib import admin
from .models import Category, SalesAd, Conversation, ConversationMessage


admin.site.register(Category)
admin.site.register(ConversationMessage)


@admin.register(SalesAd)
class SalesAdAdmin(admin.ModelAdmin):
    search_fields = ['category__name', 'title', 'author', 'seller__username', 'city', 'description']
    list_filter = ['sold']

    # Function that modifies the queryset and returns it if sold filter is on so that admin can search amongst sold ads.
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        if 'sold' in request.GET:
            queryset = queryset.filter(sold=True)

        return queryset, use_distinct


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    search_fields = ['members__username', 'ad__title']