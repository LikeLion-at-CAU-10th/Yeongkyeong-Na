from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

# Create your views here.
from .models import Likelion

class LikelionCreateView(CreateView):
    model = Likelion
    fields = "__all__"
    #fields = ['name', ]
    success_url = "/likelion/list"

class LikelionListView(ListView):
    model = Likelion
    paginate_by = 30
    ordering = ['-name']

class LikelionUpdateView(UpdateView):
    model = Likelion
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = "/likelion/list"

class LikelionDeleteView(DeleteView):
    model = Likelion
    success_url="/likelion/list"

class LikelionDetailView(DetailView):
    model = Likelion
    success_url = "/likelion"