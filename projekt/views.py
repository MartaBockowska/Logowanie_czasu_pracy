from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WorkingReportForm
from .models import Employee, Manager, Team, Project, WorkingTime


# Create your views here.

def index_view(request):
    return render(request, 'index.html')


def employees_view(request):
    employee_list = Employee.objects.all()
    employee_name = Employee.__name__
    return render(request, 'list_template.html', {'all': employee_list, 'title': employee_name})


def managers_view(request):
    manager_list = Manager.objects.all()
    manager_name = Manager.__name__
    return render(request, 'list_template.html', {'all': manager_list, 'title': manager_name})


@login_required
def add_worktime_report(request):
    form = WorkingReportForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(index_view)
    return render(request, 'work_time_form.html', {'form': form})


def project_view(request):
    project_list = Project.objects.all()
    project_name = Project.__name__
    return render(request, 'list_template.html', {'all': project_list, 'title': project_name})


def teams_view(request):
    team_list = Team.objects.all()
    team_name = Team.__name__
    return render(request, 'list_template.html', {'all': team_list, 'title': team_name})


def reports_list_view(request):
    report_list = WorkingTime.objects.all()
    report_name = "Reports"
    return render(request, 'list_template.html', {'all': report_list, 'title': report_name})

