from django.shortcuts import render
from django.views import generic
from .models import SalesAd
from django.http import HttpResponse


class SalesAdList(generic.ListView):
    model = SalesAd
    queryset = SalesAd.objects.filter(sold=False).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
