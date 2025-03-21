# Generated by Django 5.1.2 on 2025-03-10 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassportApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('city_of_birth', models.CharField(max_length=100)),
                ('state_of_birth', models.CharField(max_length=100)),
                ('country_of_birth', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed'), ('separated', 'Separated')], max_length=20)),
                ('nationality', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('address_line1', models.CharField(max_length=200)),
                ('address_line2', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('id_type', models.CharField(choices=[('aadhar', 'Aadhar Card'), ('pan', 'PAN Card'), ('passport', 'Passport'), ('voter', 'Voter ID'), ('driving', 'Driving License'), ('other', 'Other')], max_length=20)),
                ('id_number', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=200)),
                ('mother_name', models.CharField(max_length=200)),
                ('father_nationality', models.CharField(max_length=100)),
                ('mother_nationality', models.CharField(max_length=100)),
                ('father_passport_number', models.CharField(blank=True, max_length=30)),
                ('mother_passport_number', models.CharField(blank=True, max_length=30)),
                ('emergency_contact_name', models.CharField(max_length=200)),
                ('emergency_contact_relationship', models.CharField(max_length=100)),
                ('emergency_contact_phone', models.CharField(max_length=20)),
                ('emergency_contact_address', models.CharField(max_length=300)),
                ('passport_type', models.CharField(choices=[('regular', 'Regular'), ('official', 'Official'), ('diplomatic', 'Diplomatic')], max_length=20)),
                ('page_count', models.CharField(choices=[('standard', 'Standard (36 pages)'), ('extra', 'Extra (60 pages)')], max_length=20)),
                ('travel_purpose', models.CharField(choices=[('tourism', 'Tourism'), ('business', 'Business'), ('study', 'Study'), ('employment', 'Employment'), ('family', 'Family Visit'), ('other', 'Other')], max_length=20)),
                ('proof_of_identity', models.JSONField(default=list)),
                ('proof_of_address', models.JSONField(default=list)),
                ('additional_documents', models.TextField(blank=True)),
                ('payment_method', models.JSONField(default=list)),
                ('expedited_service', models.BooleanField(default=False)),
                ('signature_file', models.ImageField(upload_to='signatures/')),
                ('application_date', models.DateField()),
                ('parental_consent', models.BooleanField(default=False)),
                ('terms_agreed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application_status', models.CharField(default='draft', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='passport_documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='user_app.passportapplication')),
            ],
        ),
    ]
