from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='for_products'),
]