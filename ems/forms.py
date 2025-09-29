from django import forms
from django.utils import timezone
from phonenumber_field.formfields import PhoneNumberField

from .models import Job, Employee


# Code added for loading form data on the Booking page
class JobForm(forms.ModelForm):
    date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control form-control-sm',
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Job
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Job Title',
                    'required': True
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm',
                    'rows': 4,
                    'placeholder': 'Job Description',
                    'required': True
                }
            ),
        }


class EmployeeForm(forms.ModelForm):
    joining_date = forms.DateField(
        required=False,
        initial=timezone.now,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control form-control-sm',
                'type': 'date'
            }
        )
    )
    job = forms.ModelChoiceField(
        queryset=Job.objects.all(),
        required=True,
        empty_label="Select job for employee",
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )
    phone = PhoneNumberField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Phone',
                'required': True
            }
        )
    )

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name',
                  'email', 'phone', 'joining_date', 'job']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'First Name',
                    'required': True
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Last Name',
                    'required': True
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Email',
                    'required': True
                }
            ),
        }
