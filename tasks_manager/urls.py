
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'create/$', views.TasksCreate.as_view(), name='tasks-create'),
    url(r'update/(?P<pk>[0-9]+)/$', views.TasksUpdate.as_view(), name='tasks-update'),
    url(r'delete/(?P<pk>[0-9]+)/$', views.TasksDelete.as_view(), name='tasks-delete'),
    url(r'^$', views.TasksList.as_view(), name='tasks-list'),
]
