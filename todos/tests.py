from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Todos

class TodosTestCase(TestCase):
    def test_create_todo(self):
        todo = Todos.objects.create(title='Test Todo', completed=False, priority=2)
        self.assertEqual(todo.title, 'Test Todo')
        self.assertEqual(todo.completed, False)
        self.assertEqual(todo.priority, 2)

    def test_todo_validation_error(self):
        with self.assertRaises(ValidationError):
            todo = Todos.objects.create(title='Test Todo', completed=False, priority=5)
            todo.full_clean()

    def test_todo_str(self):
        todo = Todos.objects.create(title='Test Todo', completed=False, priority=2)
        self.assertEqual(str(todo), todo.title)

    def test_todo_absolute_url(self):
        todo = Todos.objects.create(title='Test Todo', completed=False, priority=2)
        url = todo.get_absolute_url()
        self.assertEqual(url, f'/todos/{todo.id}/')

import pytest
from django.core.exceptions import ValidationError
from .models import Todos

@pytest.mark.django_db
def test_create_todo():
    todo = Todos.objects.create(title='Test Todo', completed=False, priority=2)
    assert todo.title == 'Test Todo'
    assert todo.completed == False
    assert todo.priority == 2

@pytest.mark.django_db
def test_todo_validation_error():
    with pytest.raises(ValidationError):
        todo = Todos.objects.create(title='Test Todo', completed=False, priority=5)
        todo.full_clean()

@pytest.mark.django_db
def test_todo_str():
    todo = Todos.objects.create(title='Test Todo', completed=False, priority=2)
    assert str(todo) == todo.note

@pytest.mark.django_db
def test_todo_absolute_url():
    todo = Todos.objects.create(title='Test Todo', completed=False, priority=2)
    url = todo.get_absolute_url()
    assert url == f'/todos/{todo.id}/'

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestTodosAPI:

    @pytest.fixture
    def api_client(self):
        return APIClient()

    def test_list_todos(self, api_client):
        response = api_client.get('/todos/v1/api/')
        assert response.status_code == 200

    def test_create_todo(self, api_client):
        data = {
            'title': 'Test Todo',
            'completed': False,
            'priority': 1
        }
        response = api_client.post('/todos/v1/api/', data=data)
        assert response.status_code == 201

    def test_retrieve_todo_detail(self, api_client, todo):
        response = api_client.get(f'/todos/v1/api/{todo.id}/')
        assert response.status_code == 200

    def test_update_todo_detail(self, api_client, todo):
        data = {
            'title': 'Updated Todo',
            'completed': True,
            'priority': 2
        }
        response = api_client.patch(f'/todos/v1/api/{todo.id}/', data=data)
        assert response.status_code == 200

    def test_delete_todo_detail(self, api_client, todo):
        response = api_client.delete(f'/todos/v1/api/{todo.id}/')
        assert response.status_code == 204

from rest_framework.test import APITestCase


class TodosAPITestCase(APITestCase):

    def test_list_todos(self):
        response = self.client.get('/todos/v1/api/')
        self.assertEqual(response.status_code, 200)

    def test_create_todo(self):
        data = {
            'title': 'Test Todo',
            'completed': False,
            'priority': 1
        }
        response = self.client.post('/todos/v1/api/', data=data)
        self.assertEqual(response.status_code, 201)

    def test_retrieve_todo_detail(self, todo):
        response = self.client.get(f'/todos/v1/api/{todo.id}/')
        self.assertEqual(response.status_code, 200)


from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Todos

class TodosTestCase(TestCase):
    def test_create_todo(self):
        todo = Todos.objects.create(title='Test Todo', completed=False, priority=2)
        self.assertEqual(todo.title, 'Test Todo')
        self.assertEqual(todo.completed, False)
        self.assertEqual(todo.priority, 2)

    def test_todo_validation_error(self):
        with self.assertRaises(ValidationError):
            todo = Todos.objects.create(title='Test Todo', completed=False, priority=5)
            todo.full_clean()

    def test_todo_str(self):
        todo = Todos.objects.create(title='Test Todo', completed=False, priority=2)
        self.assertEqual(str(todo), todo.note)

    def test_todo_absolute_url(self):
        todo = Todos.objects.create(title='Test Todo', completed=False, priority=2)
        url = todo.get_absolute_url()
        self.assertEqual(url, f'/todos/{todo.id}/')
