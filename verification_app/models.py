from django.db import models

# Create your models here.
from django.db import models
from user_app.models import PassportApplication     
from django.contrib.auth.hashers import make_password, check_password
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
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.employee_id})'
  
    
class PassportVerification(models.Model):
    VERIFIED = 'Verified'
    REJECTED = 'Rejected'
    VERIFICATION_STATUS_CHOICES = [
        (VERIFIED, 'Verified'),
        (REJECTED, 'Rejected'),
    ]

    ADMIN_PENDING = 'Pending'
    ADMIN_APPROVED = 'Approved'
    ADMIN_REJECTED = 'Rejected'
    ADMIN_VERIFICATION_CHOICES = [
        (ADMIN_PENDING, 'Pending'),
        (ADMIN_APPROVED, 'Approved'),
        (ADMIN_REJECTED, 'Rejected'),
    ]

    application_id = models.CharField(max_length=20, unique=True)
    passport_application = models.ForeignKey(PassportApplication, on_delete=models.CASCADE)
    verification_officer = models.ForeignKey(Employee, on_delete=models.CASCADE)
    verification_date_time = models.DateTimeField(auto_now=True)
    verification_status = models.CharField(max_length=20, choices=VERIFICATION_STATUS_CHOICES, blank=True, null=True)  # Limit to Verified/Rejected
    remarks = models.TextField(blank=True, null=True)
    admin_verification = models.CharField(max_length=20, choices=ADMIN_VERIFICATION_CHOICES,  blank=True, null=True)  # Limit to Pending/Approved/Rejected
    admin_remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Verification for {self.application_id}"

