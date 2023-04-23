from django.shortcuts import render
from django.views import generic
from .models import SalesAd


class SalesAdList(generic.ListView):
    model = SalesAd
    queryset = SalesAd.objects.filter(sold=False).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
