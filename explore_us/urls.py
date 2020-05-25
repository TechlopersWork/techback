from django.urls import path
from . import views

urlpatterns = [
    path("", views.explore, name='for_explore'),
    # path('products/', views.products),
]