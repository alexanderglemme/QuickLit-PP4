from django.urls import path
from . import views


urlpatterns = [
    path('', views.SalesAdList.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<slug:slug>/', views.SalesAdDetail.as_view(), name='detail'),
    
]
