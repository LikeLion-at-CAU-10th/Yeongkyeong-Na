from django.urls import path
from .views import LikeLionCreateView, LikeLionDeleteView, LikeLionUpdateView, LikeLionListView
urlpatterns = [
    # path('', likelion_form_create, name ="likelion_main"),
    # path('create/', likelion_create, name="likelion_create"),
    # path('list/', likelion_list_all, name="likelion_list_all"),
    path('list/', LikeLionListView.as_view(), name="likelion_list_all"),
    path('create/', LikeLionCreateView.as_view(), name="likelion_create"),

]
# 조회, 수정, 삭제