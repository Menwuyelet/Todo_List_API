from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import User

# Create your tests here.

class AuthAPItest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.user = User.objects.create_user(
            email = 'testuser@example.com',
            password = 'testpass'
        )

    def test_registration(self):
        data = {
            'email' : 'newuser@example.com',
            'password' : 'newpass'
        }

        response = self.client.post(reverse('signup'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.filter(email = 'newuser@example.com').count(), 1)
        
    def test_register_duplicate_user(self):
        data = {
            'email': 'newuser1@example.com',
            'password': 'newpass'
        }

        response = self.client.post(reverse('signup'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.filter(email = 'newuser1@example.com').count(), 1)

        duplicate_response = self.client.post(reverse('signup'), data)

        self.assertEqual(duplicate_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.filter(email = 'newuser1@example.com').count(), 1)

    def test_register_invalid_user(self):
        data = {
            'email': 'newuser@example',
            'password': 'newpass'
        }

        response = self.client.post(reverse('signup'), data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.filter(email = 'newuser@example').count(), 0)

    def test_login_user(self):
        data = {
            'email' : 'testuser@example.com',
            'password' : 'testpass'
        }

        response = self.client.post(reverse('login'), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid_user(self):
        data = {
            'email': 'testuser1r@example.com',
            'password': 'newpass'
        }

        response = self.client.post(reverse('login'), data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("No active account found with the given credentials", response.data['detail'])
    
    def test_refresh_token(self):
        data = {
            'email' : 'testuser@example.com',
            'password' : 'testpass'
        }

        login_response = self.client.post(reverse('login'), data)
        ref_token = login_response.data['refresh']

        response = self.client.post(reverse('token_refresh'), {'refresh': ref_token})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_invalid_refresh(self):
        refresh = "Invalid refresh token"
        

        response = self.client.post(reverse('token_refresh'), {'refresh' : refresh})

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('token_not_valid', response.data['code'])

    def test_logout(self):
        login_data = {
            'email' : 'testuser@example.com',
            'password' : 'testpass'
        }
        login_response = self.client.post(reverse('login'), login_data)

        access_token = login_response.data['access']
        refresh_token = login_response.data['refresh']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        logout_response = self.client.post(reverse('logout'), data={'refresh': refresh_token})

        self.assertEqual(logout_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_user(self):
        login_data = {
            'email' : 'testuser@example.com',
            "password" : 'testpass'
        }

        login_response = self.client.post(reverse('login'), login_data)
        access_token = login_response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        response = self.client.delete(reverse('delete_user'))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.filter(email = "testuser@example.com").count(), 0)

    def test_delete_unauthenticated_user(self):
        response = self.client.post(reverse('delete_user'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("Authentication credentials were not provided", response.data['detail'])

        error_detail = response.data["detail"]
        self.assertEqual(error_detail.code, 'not_authenticated') 




############ Check the reverse name error causeing tests to fail.###############cc