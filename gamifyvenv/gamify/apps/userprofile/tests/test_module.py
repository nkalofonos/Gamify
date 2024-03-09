from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from apps.userprofile.forms import SignUpForm


class SignupIntegrationTest(TestCase):
    def setUp(self):
        self.test_user_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }

    def test_signup_view(self):
        client = Client()

        url = reverse('signup')

        response = client.post(url, data=self.test_user_data, follow=True)

        self.assertRedirects(response, reverse('frontpage'))

        self.assertTrue(User.objects.filter(username=self.test_user_data['username']).exists())


    def test_signup_form_validation(self):
        invalid_data = {
            'username': '',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'incalid-email', 
            'password1': 'testpassword123',
            'password2': 'testpassword456',
        }

        form = SignUpForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('password2', form.errors)


