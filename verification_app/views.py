from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee,PassportApplication

from django.shortcuts import render, redirect
from .forms import EmployeeForm
from django.contrib import messages
import logging

# Set up logging
logger = logging.getLogger(__name__)

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Registration submitted successfully!')
                return redirect('login_verifer')  # Replace 'login' with your login URL name
            except Exception as e:
                logger.error(f"Error saving employee: {e}")
                messages.error(request, 'There was an error saving your data. Please try again.')
        else:
            # Log form errors for debugging
            logger.error(f"Form errors: {form.errors}")
            messages.error(request, 'Invalid form submission. Please correct the errors below.')
    else:
        form = EmployeeForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):

        # Render the login page
        return render(request,'login_verifer.html')

def login_verifer_method(request):
     if request.method == 'POST':
        employee_id = request.POST.get('employeeId')
        password = request.POST.get('password')

        try:
            # Fetch the employee based on the provided employee ID
            employee = Employee.objects.get(employee_id=employee_id)

            # Check if the password matches (you should hash passwords in a real application)
            if employee.password == password:
                # Successful login
                # You can set session variables or redirect to the dashboard
                request.session['employee_id'] = employee.employee_id  # Store employee ID in session
                return redirect(dashboard_verifier_view)  # Redirect to the dashboard page
            else:
                messages.error(request, 'Invalid password. Please try again.')
        except Employee.DoesNotExist:
            messages.error(request, 'Employee ID not found. Please try again.')
        return redirect(login_view)

def dashboard_verifier_view(request):
    return render(request,'dashboard_verifier.html')

def status_update_view(request):
    return render(request,'status_update.html')

def list_user_view(request):
    data = PassportApplication.objects.all()
    return render(request, "officer/List_user.html",{"data": data})