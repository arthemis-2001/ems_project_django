from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.title}"

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField(unique=True, region="US")
    joining_date = models.DateField(default=timezone.now)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
