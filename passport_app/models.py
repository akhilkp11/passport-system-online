from django.db import models
# from django.contrib.auth.models import User



class PassportOfficer(models.Model):
    UserNaMe = models.CharField(max_length=100, null=True, blank=True, default="")
    PassWoRd = models.CharField(max_length=100, null=True, blank=True, default="")
    email = models.EmailField(unique=True)
    name=models.CharField(max_length=20)
    employee_id = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=15)
    branch_location = models.CharField(max_length=100,null=True,blank=True)
    assigned_region = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return self.name

class PassportVerifier(models.Model):
    name = models.CharField(max_length=100)
    UserNaMe = models.CharField(max_length=100, null=True, blank=True, default="")
    PassWoRd = models.CharField(max_length=100, null=True, blank=True, default="")
    email = models.EmailField(unique=True)
    verifier_id = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    date_of_joining = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# class PassportApplication(models.Model):
#     STATUS_CHOICES = [
#         ('submitted', 'submitted'),
#         ('In Review', 'In Review'),
#         ('Approved', 'Approved'),
#         ('Rejected', 'Rejected'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'applicant'})
#     application_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')

#     def __str__(self):
#         return f"Application {self.id} - {self.user.username}"
    


    

# class StaffManagement(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'user_type__in': ['officer', 'verifier']})
#     assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     department = models.CharField(max_length=100, choices=[('verification', 'Verification'), ('approval', 'Approval')])
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.department}"


# class ApplicationTracking(models.Model):
#     application = models.ForeignKey(PassportApplication, on_delete=models.CASCADE)
#     updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Officer/Verifier/Admin
#     status = models.CharField(max_length=20, choices=PassportApplication.STATUS_CHOICES)


# class Feedback(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     submitted_at = models.DateTimeField(auto_now_add=True)
#     admin_response = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"Feedback from {self.user.username}"
    

