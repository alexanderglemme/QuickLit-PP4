from django.urls import path
from . import views


urlpatterns = [
    path('', views.SalesAdList.as_view(), name='index'),

]
