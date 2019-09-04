from django.test import TestCase, Client
# from django.db import transaction
from ..views import TasksList 
from django.contrib.auth.models import User

C = Client()


# Create your tests here.
class SignUpTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin147', password='123456')

    def test_sign_up(self):
        response = C.post('/accounts/login/', {'username': 'admin147', 'password': '123456'})
        self.assertEqual(response.status_code, 302)


# class TasksMangerTestCase(TestCase):
#     def setUp(slef):
#         self.user =
#     def test_tasks_list(self):
        
