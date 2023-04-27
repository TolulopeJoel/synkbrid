from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from accounts.models import Team
from .models import Task
from .serializers import TaskSerializer


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpass123'
        )
        self.team = Team.objects.create(
            name='Test Team',
            assigner=self.user
        )

    def test_task_creation(self):
        task = Task.objects.create(
            team=self.team,
            name='Test Task',
            description='This is a test task',
            status='not-started',
            start_date='2023-04-27 08:00:00',
            due_date='2023-04-28 17:00:00'
        )
        self.assertEqual(str(task), 'Test Task')


class TaskViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpass123'
        )
        self.team = Team.objects.create(
            name='Test Team',
            assigner=self.user
        )
        self.team.teamates.set([self.user])

        self.task1 = Task.objects.create(
            team=self.team,
            name='Test Task 1',
            description='This is a test task',
            status='not-started',
            start_date='2023-04-27 08:00:00',
            due_date='2023-04-28 17:00:00'
        )
        self.task1.assignees.set([self.user])

        self.task2 = Task.objects.create(
            team=self.team,
            name='Test Task 2',
            description='This is another test task',
            status='not-started',
            start_date='2023-04-29 08:00:00',
            due_date='2023-04-30 17:00:00'
        )
        self.task2.assignees.set([self.user])

    def test_get_task_list(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('task-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_create_task(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('task-list')
        data = {
            'team_id': self.team.id,
            'name': 'New Test Task',
            'description': 'This is a new test task',
            'status': 'not-started',
            'start_date': '2023-05-01 08:00:00',
            'due_date': '2023-05-02 17:00:00',
            'assignees_username': f'{self.user.username}'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)

    def test_update_task(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('task-detail', args=[self.task1.id])
        data = {'status': 'in-progress'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=self.task1.id).status, 'in-progress')

    def test_delete_task(self):
        self.client.force_authenticate(user=self.user)
        url1 = reverse('task-detail', args=[self.task1.id])
        url2 = reverse('task-detail', args=[self.task2.id])
        response1 = self.client.delete(url1, format='json')
        response2 = self.client.delete(url2, format='json')
        self.assertEqual(response1.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response2.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
       
