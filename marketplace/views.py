from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from .models import SalesAd


class SalesAdList(generic.ListView):
    model = SalesAd
    queryset = SalesAd.objects.filter(sold=False).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class SlesAdDetail(View):

    def get(self, request, slug, *args, **kwargs):
        """
        Get method for retrieving a particular record
        """
        queryset = SalesAd.objects.filter(sold=False)
        sales_ad = get_object_or_404(queryset, slug=slug)
        template_name = 'sales_ad_single.html'
        context = {
            'salesad': salesad
        }
        return render(request, template_name, context)
