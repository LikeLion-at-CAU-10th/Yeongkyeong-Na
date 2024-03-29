"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('list/', LikelionListView.as_view(), name="likelion_list_all"),
    path('create/', LikelionCreateView.as_view(), name="likelion_create"),
    path('detail/<int:pk>', LikelionDetailView.as_view(), name="likelion_detail"),
    path('delete/<int:pk>', LikelionDeleteView.as_view(),name="likelion_delete"),
    path('update/<int:pk>', LikelionUpdateView.as_view(), name="likelion_update"),
]
