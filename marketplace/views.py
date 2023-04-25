from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import SalesAd
from .forms import SignUpForm, NewAdForm


class SalesAdList(generic.ListView):
    model = SalesAd
    queryset = SalesAd.objects.filter(sold=False).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class SalesAdDetail(View):

    def get(self, request, slug, *args, **kwargs):
        """
        Gets a single ad
        """
        queryset = SalesAd.objects.filter(sold=False).order_by('-created_on')
        sales_ad = get_object_or_404(queryset, slug=slug)
        template_name = 'sales_ad_detail.html'
        context = {
            'ad': sales_ad
        }
        return render(request, template_name, context)


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class NewAdView(CreateView):
    model = SalesAd
    form_class = NewAdForm
    template_name = 'new_sales_ad.html'
    success_url = reverse_lazy('newad')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
