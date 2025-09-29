from django.shortcuts import render, redirect
from .models import Job, Employee
from .forms import JobForm, EmployeeForm

# Create your views here.
def dash(request):
    employee_count = Employee.objects.count()
    job_count = Job.objects.count()
    context = {"employee_count": employee_count, "job_count": job_count}
    return render(request, "dash.html", context)


def jobs(request):
    jobs = Job.objects.all().order_by("date")
    
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jobs")
    
    context = {"jobs": jobs, "form": form}
    return render(request, "jobs.html", context)


def employees(request):
    employees = Employee.objects.select_related(
        "job").all().order_by("joining_date")
    
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employees")
    
    context = {"employees": employees, "form": form}
    return render(request, "employees.html", context)
