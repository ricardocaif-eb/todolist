from django.test import TestCase
from django.db import transaction
from ..models import Priority, TasksManager
from django.contrib.auth.models import User


# Create your tests here.
class PriorityTestCase(TestCase):
    def setUp(self):
        self.p1 = Priority.objects.create(priority='low')
        self.p2 = Priority.objects.create(priority='normal')
        self.p3 = Priority.objects.create(priority='high')

    def test_priorities_length(self):
        priorities = Priority.objects.all()
        self.assertEqual(len(priorities), 3)

    def test_property_str(self):
        self.assertEqual(str(self.p1), 'low')

    def test_property_attributes(self):
        self.assertEqual(self.p1.priority, 'low')


class TasksManagerTestCase(TestCase):
    def setUp(self):
        self.task = {
            'name': 'test1',
            'user': User.objects.create_user(username='admin', password='admin', is_staff=True, is_superuser=True),
            'priority': Priority.objects.create(priority='normal')
            }

    def test_creating_task(self):
        try:
            with transaction.atomic():
                TasksManager.objects.create()
        except Exception:
            pass

        task = TasksManager.objects.create(**self.task)
        self.assertEqual(task.name, 'test1')
