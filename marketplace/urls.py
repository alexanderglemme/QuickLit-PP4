from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm


urlpatterns = [
    path('', views.SalesAdList.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('new-sales-ad/', views.NewAdView.as_view(), name='newad'),
    path('<slug:slug>/', views.SalesAdDetail.as_view(), name='detail'),
    
    
]
