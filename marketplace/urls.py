from django.conf.urls import handler404
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm


urlpatterns = [
    path('', views.SalesAdList.as_view(), name='index'),
    path('new-group/', views.NewStudyGroupView.as_view(), name='new_group'),
    path('about/', views.AboutQuickLitView.as_view(), name='about'),
    path('search/', views.SearchAdsView.as_view(), name='search'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('new-sales-ad/', views.NewAdView.as_view(), name='newad'),
    path('profile/', views.ProfileOverviewView.as_view(), name='profile'),
    path('inbox/', views.InboxView.as_view(), name='inbox'),
    path('new-chat/<int:ad_pk>/', views.NewConversationView.as_view(), name='new_chat'),
    path('active-group/<slug:slug>', views.ActiveStudyGroupView.as_view(), name='active_group'),
    path('active/<int:pk>/', views.ActiveConversationView.as_view(), name='active'),
    path('edit/<slug:slug>/', views.EditSalesAdView.as_view(), name='editad'),
    path('delete/<slug:slug>/', views.DeleteAdView.as_view(), name='delete'),
    path('delete-group/<slug:slug>', views.DeleteStudyGroupView.as_view(), name='delete_group'),
    path('<slug:slug>/', views.SalesAdDetail.as_view(), name='detail'),
]

handler404 = 'marketplace.views.custom_404'
