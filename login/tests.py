from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class RegisterTestCase(TestCase):
    def test_user_registration(self):
        response= self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
        })
        self.assertEqual(response.status_code, 302)  # Redirects to login
        self.assertTrue(User.objects.filter(username= 'testuser').exists())

    def test_registration_password_mismatch(self):
        response= self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'pass1',
            'password2': 'pass2',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Password not matching')

class LoginTestCase(TestCase):
    def setUp(self):
        self.user= User.objects.create_user(username= 'demo', password='demopass')

    def test_login_success(self):
        response= self.client.post(reverse('login'), {
            'username': 'demo',
            'password': 'demopass'
        })
        self.assertRedirects(response, reverse('profile'))
    
    def test_logout(self):
        self.client.login(username= 'demo', password= 'demopass')
        response= self.client.get(reverse('logout'))
        self.assertRedirects(response, '/')

    def test_login_failure(self):
        response= self.client.post(reverse('login'), {
            'username': 'wrong',
            'password': 'wrongpass'
        })
        self.assertContains(response, 'Invalid credentials')




   