from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class LogInIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password',
        )

    def test_valid_login(self):
        invalid_data = {
            'username': 'testuser',
            'password': 'password',
        }

        url = reverse('login')
        response = self.client.post(url, invalid_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.wsgi_request.user.is_authenticated)


    def test_invalid_login(self):
        invalid_data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }

        url = reverse('login')
        response = self.client.post(url, invalid_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
