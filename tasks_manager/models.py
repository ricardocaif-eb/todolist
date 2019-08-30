from django.conf import settings
from django.db import models

# Create your models here.


class Priority(models.Model):
    priority = models.CharField(max_length=20)

    def __str__(self):
        return self.priority


class TasksManager(models.Model):
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    event_id = models.CharField(max_length=200)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None
        )
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
