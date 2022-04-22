import pytest
from django.urls import reverse

from projekt.views import employees_view, managers_view, index_view, project_view, teams_view
from projekt.models import Employee, Manager, Project, Team

username = "admin"
password = "admin"


@pytest.mark.django_db
def test_lists_all_employees(client, django_user_model):
    user=django_user_model.objects.create_user(username=username, password=password)
    Employee.objects.create(first_name="Jan", last_name="Nowak", user=user)
    response = client.get(reverse('employee'))
    assert len(response.context['all']) == 1

@pytest.mark.django_db
def test_lists_all_managers(client, django_user_model):
    user=django_user_model.objects.create_user(username=username, password=password)
    Manager.objects.create(first_name="Jan", last_name="Nowak", user=user)
    response = client.get(reverse('manager'))
    assert len(response.context['all']) == 1

@pytest.mark.django_db
def test_lists_all_projects(client, django_user_model):
    user=django_user_model.objects.create_user(username=username, password=password)
    manager=Manager.objects.create(first_name="Jan", last_name="Nowak", user=user)
    Project.objects.create(name="test", tasks="123", manager=manager)
    response = client.get(reverse('project'))
    assert len(response.context['all']) == 1

@pytest.mark.django_db
def test_lists_all_teams(client, django_user_model):
    user=django_user_model.objects.create_user(username=username, password=password)
    user2= django_user_model.objects.create_user(username='username', password='password')
    manager=Manager.objects.create(first_name="Jan", last_name="Nowak", user=user)
    employee = Employee.objects.create(first_name="Jan", last_name="Nowak", user=user)
    employee_2 = Employee.objects.create(first_name="username", last_name="password", user=user2)
    project = Project.objects.create(name="test", tasks="123", manager=manager)
    team=Team(name='Team', manager=manager, project=project)
    team.save()
    team.employee.add(employee)
    team.employee.add(employee_2)
    team.save()
    response = client.get(reverse('team'))
    assert len(response.context['all']) == 1


@pytest.mark.django_db
def test_report_with_authenticated_client(client, django_user_model):
    username = "admin"
    password = "admin"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    response = client.get('/working-time')
    assert response.status_code == 200


@pytest.mark.django_db
def test_report_without_authenticated_client(client):
    response = client.get('/working-time')
    assert response.status_code != 200


