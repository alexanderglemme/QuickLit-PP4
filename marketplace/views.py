from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator

from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import SalesAd, User, Conversation, StudyGroup
from .forms import SignUpForm, NewAdForm, SalesAdForm, ConversationMessageForm, NewStudyGroupForm


class SearchAdsView(View):
    """
    Searches sales ads based on the users query
    and gets the ads containing said query
    """
    def get(self, request):
        query = self.request.GET.get('query', '')
        ads = SalesAd.objects.filter(sold=False)

        if query:
            ads = ads.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(author__icontains=query) |
                Q(city__icontains=query) |
                Q(category__name__icontains=query) |
                Q(seller__username__icontains=query)
            )

        paginator = Paginator(ads, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'search_ads.html', {
            'page_obj': page_obj,
            'query': query,
        })


class SalesAdList(generic.ListView):
    """
    Gets a list of all unsold ads in the order of newest to oldest.
    """
    model = SalesAd
    queryset = SalesAd.objects.filter(sold=False).order_by('-created_on')
    template_name = 'index.html'


class SalesAdDetail(View):
    """
    Gets a single ad
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Gets a single ad
        """
        queryset = SalesAd.objects.order_by('-created_on')
        sales_ad = get_object_or_404(queryset, slug=slug)
        template_name = 'sales_ad_detail.html'
        context = {
            'ad': sales_ad
        }
        return render(request, template_name, context)


class SignUpView(CreateView):
    """
    View for signing up to QuickLit, utilizing the SignUpForm
    which inherits from djangos UserCreationForm
    """
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
    of the SalesAd entry if the user is the seller
    and redirects to the detail view of the edited ad
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
            if sales_ad.sold:
                return redirect('profile')
            else:
                pass

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


class DeleteAdView(LoginRequiredMixin, DeleteView):
    """
    Deletes a chosen SalesAd if the user is logged in,
    only the logged in users ads are reachable
    and if by som very unlikely reason
    the seller is not the user it raises 404.
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


class NewConversationView(LoginRequiredMixin, CreateView):
    """
    Gets the ads id, makes a new conversation object
    setting the members of the new conversation
    to the logged in user and the ads seller
    and sets the conversations id to the
    ads pk, also saves the message.
    """
    def get(self, request, ad_pk):
        ad = get_object_or_404(SalesAd, pk=ad_pk)

        if ad.seller == request.user:
            return redirect('profile')

        conversations = Conversation.objects.filter(ad=ad).filter(members__in=[request.user.id])

        if conversations:
            return redirect('active', ad_pk)

        form = ConversationMessageForm()

        return render(request, 'new_chat.html', {
            'form': form
        })

    def post(self, request, ad_pk):
        ad = get_object_or_404(SalesAd, pk=ad_pk)

        if ad.seller == request.user:
            return redirect('profile')

        conversations = Conversation.objects.filter(ad=ad).filter(members__in=[request.user.id])

        if conversations:
            return redirect('active', ad_pk)

        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(ad=ad)
            conversation.members.add(request.user)
            conversation.members.add(ad.seller)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('inbox')

        return render(request, 'new_chat.html', {
            'form': form
        })


class InboxView(LoginRequiredMixin, View):
    """
    Gets all conversation objects and study group objects which members field
    contains the logged in user
    """

    def get(self, request):
        study_groups = StudyGroup.objects.filter(members__in=[self.request.user.id])
        conversations = Conversation.objects.filter(members__in=[self.request.user.id])

        return render(request, 'inbox.html', {
            'conversations': conversations,
            'study_groups': study_groups
        })


class ActiveConversationView(LoginRequiredMixin, View):
    """
    Gets the conversation that the logged in user is a member in,
    gets the form in which the user makes a message in,
    posts the message to the conversation object and saves it,
    enabling users to chat back and forth.
    """

    def get(self, request, pk):
        conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
        form = ConversationMessageForm()
        return render(request, 'active_conversation.html', {
            'conversation': conversation,
            'form': form
        })

    def post(self, request, pk):
        conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('active', pk=pk)

        return render(request, 'active_conversation.html', {
            'conversation': conversation,
            'form': form
        })


class NewStudyGroupView(LoginRequiredMixin, CreateView):
    """
    View to create a study group
    """
    model = StudyGroup
    form_class = NewStudyGroupForm
    template_name = 'new_study_group.html'
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        study_group = form.save(commit=False)
        study_group.save()
        selected_members = form.cleaned_data['search_members']

        for member in selected_members:
            study_group.members.add(member)

        study_group.members.add(self.request.user)
        study_group.save()
        return super().form_valid(form)


class ActiveStudyGroupView(LoginRequiredMixin, View):
    """
    Gets the  that the study group if logged in user is a member in it,
    gets the form in which the user makes a message in,
    posts the message to the study group object and saves it,
    enabling users to chat back and forth.
    """

    def get(self, request, slug):
        study_group = StudyGroup.objects.filter(members__in=[request.user.id]).get(slug=slug)
        form = ConversationMessageForm()
        return render(request, 'active_study_group.html', {
            'study_group': study_group,
            'form': form
        })

    def post(self, request, slug):
        study_group = StudyGroup.objects.filter(members__in=[request.user.id]).get(slug=slug)
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.study_group = study_group
            conversation_message.created_by = request.user
            conversation_message.save()

            study_group.save()

            return redirect('active_group', slug=slug)

        return render(request, 'active_study_group.html', {
            'study_group': study_group,
            'form': form
        })


class DeleteStudyGroupView(LoginRequiredMixin, DeleteView):
    """
    Deletes a chosen study group. Checks that user is member before deletion.
    """
    model = StudyGroup
    template_name = 'delete_study_group.html'
    success_url = reverse_lazy('inbox')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        for member in obj.members.all():
            if Q(member__icontains=self.request.user):
                return obj
            else:
                raise Http404

    def delete(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)

# class NewStudyGroupView(LoginRequiredMixin, CreateView):
#     """
#     View to create a study group which is basically a group chat
#     """
#     def get(self, request):

#         form = StudyGroupForm()

#         return render(request, 'new_study_group.html', {
#             'form': form
#         })

#     def post(self, request, pk):

#         study_group = StudyGroup.objects.filter(members__in=[request.user.id])

#         if study_group:
#             return redirect('active_group', pk)

#         form = StudyGroupForm(request.POST)

#         if form.is_valid():
#             study_group = StudyGroup.objects.create(pk=pk)
#             study_group.save()

#             return redirect('inbox')

#         return render(request, 'new_study_group.html', {
#             'form': form
#         })


class AboutQuickLitView(TemplateView):
    template_name = 'about.html'


def custom_404(request, exception):
    """
    Handles HTTP 404 errors
    """
    template_name = '404.html'
    return render(request, template_name, status=404)
