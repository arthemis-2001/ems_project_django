from django.shortcuts import render
from .models import Job

# Create your views here.
def dash(request):
    return render(request, "dash.html")

def jobs(request):
    jobs_data = Job.objects.all().order_by("date")
    data = {"jobs": jobs_data}
    return render(request, "jobs.html", data)

def employees(request):
    return render(request, "employees.html")