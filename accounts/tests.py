from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from .models import Team

class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name='test team',
            assigner=get_user_model().objects.create_user(
                username='testuser',
                email='testuser1@example.com',
                password='testpassword'
                ),
        )

    def test_team_name(self):
        self.assertEqual(str(self.team), 'test team')

    def test_team_assigner(self):
        self.assertEqual(self.team.assigner.email, 'testuser1@example.com')

class TeamViewsetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser2@example.com',
            password='testpassword'
        )
        self.user2 = get_user_model().objects.create_user(
            username='testuser23',
            email='testuser1@example.com',
            password='testpassword'
        )
        self.team = Team.objects.create(
            name='test team',
            assigner=self.user,
        )
        self.team.teamates.set([self.user, self.user2])

    def test_create_team(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('team-list')
        data = {
            'name': 'new team',
            'teamate_emails': 'testuser1@example.com,testuser2@example.com',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'new team')
        self.assertEqual(len(response.data['teamates']), 2)

    def test_get_team_list(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('team-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'test team')
        self.assertEqual(len(response.data['results'][0]['teamates']), 2)

class CustomTokenObtainPairViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser3@example.com',
            password='testpassword'
        )

    def test_create_token(self):
        url = reverse('token_obtain_pair')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        url = reverse('register')
        data = {    
            'username': 'testuserNew',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'testuser4@example.com',
            'password': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email='testuser4@example.com')
        self.assertTrue(user.check_password('testpassword'))
