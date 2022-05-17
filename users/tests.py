from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
        username='will',
        email='will@email.com',
        password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        print("Create User good")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
        username='superadmin',
        email='superadmin@email.com',
        password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        print("Create SuperUser good")

class SignUpPageTests(TestCase): 
    def setUp(self):
        self.response = self.client.get(reverse('account_signup'))
    def test_signup_status(self): 
        self.assertEqual(self.response.status_code, 200)
    def test_signup_template(self): 
        self.assertTemplateUsed(self.response, "account/signup.html")