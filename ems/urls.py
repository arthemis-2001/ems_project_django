from django.urls import path
from . import views


urlpatterns = [
    path("dash/", views.dash, name="dash"),
    path("jobs/", views.employees, name="jobs"),
    path("employees/", views.employees, name="employees"),
]