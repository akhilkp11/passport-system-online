# Generated by Django 5.1.6 on 2025-03-05 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('passport_app', '0002_remove_passportverifier_user_delete_passportofficer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassportOfficer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserNaMe', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('PassWoRd', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('employee_id', models.CharField(max_length=10, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('branch_location', models.CharField(blank=True, max_length=100, null=True)),
                ('assigned_region', models.CharField(max_length=100)),
                ('date_of_joining', models.DateField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=50)),
            ],
        ),
    ]
