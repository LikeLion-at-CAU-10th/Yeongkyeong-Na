from django.urls import path
from .views import *

urlpatterns = [
    path('create-profile/<int:family_id>', create_profile, name="create-profile"),
    path('get-profile-all/',get_profile_all, name='get-profile-all'),
    path('get-profile/<int:id>',get_profile, name='get-profile'),
    path('update-profile/<int:id>',update_profile, name='update-profile'),
    path('delete-profile/<int:id>',delete_profile, name='delete-profile'),
    path('create-family/', create_family, name="create-family"),
    path('get-family-all/', get_family_all, name='get-family-all'),
    path('delete-family/<int:id>', delete_family, name='delete-family'),
]