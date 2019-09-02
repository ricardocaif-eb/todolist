from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from eventbrite import Eventbrite
from .models import TasksManager

# Create your views here.


class TasksList(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return TasksManager.objects.filter(user=self.request.user)

    def get_events(self):
        social = self.request.user.social_auth.filter(provider='eventbrite')[0]
        token = social.access_token
        eventbrite = Eventbrite(token)
        event = eventbrite.get('/users/me/events')['events']
        return event

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # events = self.get_events()
        # events_ids = [event.id for event in events]
        # tasks = get_queryset()
        # for event in context['events_list']:
        #     event['tasks'] =
        context['events_list'] = self.get_events()
        return context


class TasksCreate(LoginRequiredMixin, CreateView):
    model = TasksManager
    fields = ['name', 'priority']
    success_url = reverse_lazy('tasks-list')

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        self.object = form.save(commit=False)
        self.object.event_id = self.kwargs['event_id']
        self.object.user = self.request.user
        return super(TasksCreate, self).form_valid(form)


class TasksUpdate(LoginRequiredMixin, UpdateView):
    model = TasksManager
    fields = ['name', 'done', 'priority']
    success_url = reverse_lazy('tasks-list')


class TasksDelete(LoginRequiredMixin, DeleteView):
    model = TasksManager
    success_url = reverse_lazy('tasks-list')
