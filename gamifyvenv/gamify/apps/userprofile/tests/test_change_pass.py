from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class ChangePassIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='old_password',
        )

    def test_change_password_view(self):
        self.client.login(username='testuser', password='old_password')
        response = self.client.post(
            reverse('myaccount'),
            {
                'old_password': 'old_password',
                'new_password1': 'new_password',
                'new_password2': 'new_password',
            }
        )
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(User.objects.get(username='testuser').check_password('new_password'))