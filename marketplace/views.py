from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import SalesAd, User
from .forms import SignUpForm, NewAdForm, SalesAdForm


class SearchAdsView(View):
    """
    Searches sales ads, and displays them based on the query
    """
    def get(self, request):
        query = request.GET.get('query', '').replace('+', '-')
        ads = SalesAd.objects.filter(sold=False)

        if query:
            ads = ads.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(category__icontains=query) | Q(seller__icontains=query) | Q(author__icontains=query))

        return render(request, 'search_ads.html', {
            'ads': ads,
            'query': query,
        })


class SalesAdList(generic.ListView):
    """
    Gets all sales ads and displays them in order of newest-oldest.
    """
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


class NewAdView(LoginRequiredMixin, CreateView):
    """
    Adds a new sales ad
    """
    model = SalesAd
    form_class = NewAdForm
    template_name = 'new_sales_ad.html'
    success_url = reverse_lazy('newad')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class EditSalesAdView(View):
    """
    Gets the given sales ad then posts the new instance
    of a the SalesAd entry if the user is the seller
    """
    def get(self, request, slug):
        sales_ad = get_object_or_404(SalesAd, slug=slug, seller=request.user)
        form = SalesAdForm(instance=sales_ad)
        return render(request, 'edit_sales_ad.html', {'form': form})

    def post(self, request, slug):
        sales_ad = get_object_or_404(SalesAd, slug=slug, seller=request.user)
        form = SalesAdForm(request.POST, request.FILES, instance=sales_ad)
        if form.is_valid():
            form.save()

            return redirect('detail', slug=slug)
        return render(request, 'edit_sales_ad.html', {'form': form})


class ProfileOverviewView(LoginRequiredMixin, ListView):
    """
    Gets all SalesAds made by the logged in user and displays them
    """
    model = SalesAd
    template_name = 'profile_overview.html'
    context_object_name = 'ads'

    def get_queryset(self):
        return super().get_queryset().filter(seller=self.request.user)


class DeleteView(LoginRequiredMixin, DeleteView):
    """
    Deletes a chosen SalesAd if the user is logged in,
    only the logged in users ads are reachable.
    """
    model = SalesAd
    template_name = 'delete_ad.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.seller == self.request.user:
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)
