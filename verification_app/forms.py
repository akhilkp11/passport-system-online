from django import forms
from .models import Employee
from django.contrib.auth.hashers import make_password

class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = [
            'employee_id', 'govt_id', 'first_name', 'middle_name', 'last_name',
            'dob', 'gender', 'photo', 'official_email', 'alternative_email',
            'mobile_number', 'emergency_contact', 'designation', 'department',
            'location', 'branch_code', 'joining_date', 'reporting_officer',
            'employment_type', 'user_role', 'jurisdiction', 'access_level',
            'verify_authority', 'digital_signature', 'password'
        ]

    def save(self, commit=True):
        employee = super().save(commit=False)
        # Hash the password before saving
        employee.password = make_password(self.cleaned_data['password'])
        if commit:
            employee.save()
        return employee


class LoginForm(forms.Form):
    e = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))