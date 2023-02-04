from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Todo

# Create your views here.
# def index(request):
#     return HttpResponse("<h1>Hello World</h1>")

class TodoList(ListView):
    model  =Todo
    context_object_name = "tasks"
    
class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"
    
class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")
    
class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")
    
class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")