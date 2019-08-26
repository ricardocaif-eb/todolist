from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import TasksManager
from django.core.urlresolvers import reverse_lazy

# Create your views here.


class TasksList(ListView):
    model = TasksManager


class TasksCreate(CreateView):
    model = TasksManager
    fields = '__all__'
    success_url = reverse_lazy('tasks-list')


class TasksUpdate(UpdateView):
    model = TasksManager
    fields = '__all__'
    success_url = reverse_lazy('tasks-list')
