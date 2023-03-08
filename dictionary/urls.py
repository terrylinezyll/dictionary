from . import views
from django.urls import path

urlpatterns = [
    path('', views.homeview, name='home'),
    path('search', views.searchview, name='search'),
]