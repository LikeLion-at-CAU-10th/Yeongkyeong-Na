from django.urls import path
from .views import *


urlpatterns = [
    path('create-category/', create_category, name="create_category"),
    path('get-category-all/', get_category_all, name= 'get-category-all'),
]