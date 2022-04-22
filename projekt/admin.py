from django.contrib import admin
from .models import Manager, Employee, WorkingTime, Project, Team

admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(WorkingTime)
admin.site.register(Project)
admin.site.register(Team)
# Register your models here.
