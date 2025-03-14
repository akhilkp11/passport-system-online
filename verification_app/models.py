from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    govt_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='employee_photos/')
    official_email = models.EmailField(unique=True)
    alternative_email = models.EmailField(blank=True, null=True)
    mobile_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=20)
    joining_date = models.DateField()
    reporting_officer = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20)
    user_role = models.CharField(max_length=50)
    jurisdiction = models.TextField()  # Comma-separated values
    access_level = models.CharField(max_length=20)
    verify_authority = models.TextField()  # Comma-separated values
    password = models.CharField(max_length=128)
    digital_signature = models.ImageField(upload_to='digital_signatures/')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.employee_id})'
