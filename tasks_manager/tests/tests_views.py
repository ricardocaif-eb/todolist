from django.test import TestCase, Client
# from django.db import transaction
# from ..views import 
from django.contrib.auth.models import User

C = Client()


# Create your tests here.
class SignUpTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin147', password='123456')

    def test_sing_up(self):
        response = C.post('/accounts/login/', {'username': 'admin147', 'password': '123456'})
        self.assertEqual(response.status_code, 302)
