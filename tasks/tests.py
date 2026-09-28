from django.test import TestCase, Client
from django.urls import reverse
from tasks.models import Task

class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            category="Work",
            priority="High",
            status="Pending"
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(str(task), "Test Task (Pending)")

class TaskViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(
            title="Dashboard Task",
            description="Sample",
            priority="Medium",
            status="Pending"
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dashboard Task")

    def test_task_create_view(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'Description',
            'category': 'Personal',
            'priority': 'Low',
            'status': 'Pending',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_task_toggle_view(self):
        response = self.client.get(reverse('task_toggle', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, 'Completed')
