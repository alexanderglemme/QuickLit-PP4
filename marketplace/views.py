from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q

from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import SalesAd, User, DirectMessage, Chat
from .forms import SignUpForm, NewAdForm, SalesAdForm, MessageForm


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
    only the logged in users ads are reachable 
    and if the seller is not the user raises 404.
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


class ChatView(LoginRequiredMixin, SingleObjectMixin, FormMixin, TemplateView):
    model = User
    template_name = 'chat.html'
    success_url = reverse_lazy('chat')
    form_class = MessageForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=User.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = self.get_object(queryset=User.objects.all())

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        sender = self.request.user
        recipient = self.object
        context['recipient'] = recipient
        context['sender'] = sender
        context['messages'] = DirectMessage.objects.filter(sender=sender, recipient=recipient) | DirectMessage.objects.filter(sender=recipient, recipient=sender)
        context['form'] = self.get_form()
        return context

        def form_valid(self, form):
            recipient = self.object
            sender = self.request.user
            content = form.cleaned_data.get('content')
            message = DirectMessage.objects.create(sender=sender, recipient=recipient, content=content)
            message.save()
            return HttpResponseRedirect(self.get_success_url())


class InboxView(LoginRequiredMixin, TemplateView):
    template_name = 'inbox.html'

    def get(self, request, *args, **kwargs):
        # Get all chats involving logged in user
        chats = Chat.objects.filter(participants=request.user)
        chat_list = []
        for chat in chats:
            latest_dm = DirectMessage.objects.filter(chat=chat).order_by('-timestamp').first()
            chat_list.append({
                'chat': chat,
                'latest_dm': latest_dm
            })

        return render(request, self.template_name, {'chat_list': chat_list})
