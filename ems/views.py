from django.shortcuts import render
from .models import Job, Employee

# Create your views here.
def dash(request):
    employee_count = Employee.objects.count()
    job_count = Job.objects.count()
    data = {"employee_count": employee_count, "job_count": job_count}
    return render(request, "dash.html", data)


def jobs(request):
    jobs_data = Job.objects.all().order_by("date")
    data = {"jobs": jobs_data}
    return render(request, "jobs.html", data)


def employees(request):
    employees_data = Employee.objects.select_related(
        "job").all().order_by("joining_date")
    data = {"employees": employees_data}
    return render(request, "employees.html", data)
