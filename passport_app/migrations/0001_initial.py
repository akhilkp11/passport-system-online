# Generated by Django 5.1.6 on 2025-03-04 09:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PassportOfficer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('employee_id', models.CharField(max_length=10, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('designation', models.CharField(max_length=50)),
                ('branch_location', models.CharField(max_length=100)),
                ('date_of_joining', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('user', models.OneToOneField(limit_choices_to={'user_type': 'officer'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PassportVerifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verifier_id', models.CharField(max_length=10, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('designation', models.CharField(max_length=50)),
                ('assigned_region', models.CharField(max_length=100)),
                ('date_of_joining', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('user', models.OneToOneField(limit_choices_to={'user_type': 'verifier'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
