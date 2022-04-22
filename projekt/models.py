from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Manager(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    user = models.OneToOneField(User, default="", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    user = models.OneToOneField(User, default="", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class WorkingTime(models.Model):
    date = models.DateField(default=timezone.now)
    arrival = models.TimeField(null=True, blank=True)
    leaving = models.TimeField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_description = models.TextField()

    def __str__(self):
        return f"{self.employee}: {self.arrival} - {self.leaving}"

class Project(models.Model):
    name = models.CharField(max_length=64)
    tasks = models.CharField(max_length=64)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
    name = models.CharField(max_length=64)
    manager = models.OneToOneField(Manager, on_delete=models.CASCADE)
    employee = models.ManyToManyField(Employee)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"