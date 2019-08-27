from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TasksManager
from django.core.urlresolvers import reverse_lazy

# Create your views here.


class TasksList(ListView):

    def get_queryset(self):
        return TasksManager.objects.filter(user=self.request.user)


class TasksCreate(CreateView):
    model = TasksManager
    fields = ['name', 'priority']
    success_url = reverse_lazy('tasks-list')

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super(TasksCreate, self).form_valid(form)


class TasksUpdate(UpdateView):
    model = TasksManager
    fields = ['name', 'done', 'priority']
    success_url = reverse_lazy('tasks-list')


class TasksDelete(DeleteView):
    model = TasksManager
    success_url = reverse_lazy('tasks-list')
