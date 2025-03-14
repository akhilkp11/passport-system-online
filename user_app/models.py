from django.db import models

# Create your models here.


class PassportRegistration(models.Model):
    PASSPORT_TYPES = [
        ('regular', 'Regular Passport'),
        ('official', 'Official Passport'),
        ('diplomatic', 'Diplomatic Passport'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    passport_type = models.CharField(max_length=20, choices=PASSPORT_TYPES)
    terms_accepted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.passport_type}"
    
from django.db import models


class PassportApplication(models.Model):
    # Choices for dropdown fields
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
    ]
    ID_TYPE_CHOICES = [
        ('aadhar', 'Aadhar Card'),
        ('pan', 'PAN Card'),
        ('passport', 'Passport'),
        ('voter', 'Voter ID'),
        ('driving', 'Driving License'),
        ('other', 'Other'),
    ]
    
    PASSPORT_TYPE_CHOICES = [
        ('regular', 'Regular'),
        ('official', 'Official'),
        ('diplomatic', 'Diplomatic'),
    ]
    
    PAGE_COUNT_CHOICES = [
        ('standard', 'Standard (36 pages)'),
        ('extra', 'Extra (60 pages)'),
    ]
    
    TRAVEL_PURPOSE_CHOICES = [
        ('tourism', 'Tourism'),
        ('business', 'Business'),
        ('study', 'Study'),
        ('employment', 'Employment'),
        ('family', 'Family Visit'),
        ('other', 'Other'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('online', 'Online Payment (Credit/Debit Card)'),
        ('bankTransfer', 'Bank Transfer'),
        ('challan', 'Bank Challan'),
    ]
    
    # 1. Personal Information
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    city_of_birth = models.CharField(max_length=100)
    state_of_birth = models.CharField(max_length=100)
    country_of_birth = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES)
    nationality = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    
    # 2. Contact Information
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    
    # 3. Identification Details
    id_type = models.CharField(max_length=20, choices=ID_TYPE_CHOICES)
    id_number = models.CharField(max_length=100)
    
    # 4. Parental Information
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    father_nationality = models.CharField(max_length=100)
    mother_nationality = models.CharField(max_length=100)
    father_passport_number = models.CharField(max_length=30, blank=True)
    mother_passport_number = models.CharField(max_length=30, blank=True)
    
    # 5. Emergency Contact
    emergency_contact_name = models.CharField(max_length=200)
    emergency_contact_relationship = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=20)
    emergency_contact_address = models.CharField(max_length=300)
    
    # 6. Passport Type & Details
    passport_type = models.CharField(max_length=20, choices=PASSPORT_TYPE_CHOICES)
    page_count = models.CharField(max_length=20, choices=PAGE_COUNT_CHOICES)
    travel_purpose = models.CharField(max_length=20, choices=TRAVEL_PURPOSE_CHOICES)
    
    # 7. Supporting Documents
    proof_of_identity = models.JSONField(default=list)  # Stores list of selected document types
    proof_of_address = models.JSONField(default=list)   # Stores list of selected document types
    additional_documents = models.TextField(blank=True)
    
    # 8. Payment Details
    payment_method = models.JSONField(default=list)  # Stores selected payment methods
    expedited_service = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # New Field
    # 9. Declaration & Signature
    signature_file = models.ImageField(upload_to='signatures/')
    application_date = models.DateField()
    parental_consent = models.BooleanField(default=False)
    terms_agreed = models.BooleanField(default=False)
    
    # Application metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    application_status = models.CharField(max_length=20, default='draft')
    user = models.ForeignKey(PassportRegistration, on_delete=models.CASCADE, blank=True, null=True)

    
    def __str__(self):
        return f"Passport Application - {self.first_name} {self.last_name}"

class Document(models.Model):
    """Model for storing uploaded supporting documents"""
    application = models.ForeignKey(PassportApplication, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=50)
    file = models.FileField(upload_to='passport_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.document_type} for {self.application}"
    


class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('initiated', 'Initiated'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    application = models.ForeignKey(PassportApplication, on_delete=models.CASCADE, related_name='payments')
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='INR')
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='initiated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment for {self.application} - {self.status}"
