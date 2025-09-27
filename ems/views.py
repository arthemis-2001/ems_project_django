from django.shortcuts import render

# Create your views here.
def dash(request):
    return render(request, "dash.html")

def jobs(request):
    return render(request, "jobs.html")

def employees(request):
    return render(request, "employees.html")