from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee,PassportApplication, PassportVerification
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import EmployeeForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
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
        employee_id = request.POST.get('employeeId')        # geting email from login form
        password = request.POST.get('password')

        try:
            
            employee = Employee.objects.get(official_email=employee_id)
            print('employee')

            if check_password(password, employee.password):
                # Manually log in the user (since you're not using Django's default User model)
                
                request.session['emp_id'] = employee.employee_id
                print(request.session['emp_id'])
                return redirect('dashboard_verifer') 
            else:
                messages.error(request, 'Invalid password. Please try again.')
                return redirect(login_view)  # Redirect to login page

           
        except Employee.DoesNotExist:
            messages.error(request, 'Employee ID not found. Please try again.')
        return redirect(login_view)





def dashboard_verifier_view(request):
    passport_applications = PassportApplication.objects.all()
    
    emp_id = request.session.get('emp_id')
    verification_officer = Employee.objects.get(employee_id=emp_id)
    print(verification_officer.id)
    passport_verification = PassportVerification.objects.filter(verification_officer=verification_officer)
    
    print(passport_verification)
    context = {
        'passport_applications': passport_applications,
        'passport_verification': passport_verification,
    }
    return render(request,'dashboard_verifier.html', context)

def status_update_view(request, p_id):
    pssport_verification = PassportVerification.objects.get(id=p_id)    
    # passport_application = pssport_verification.passport_application

    # if request.method == 'POST':
    #     verification_status = request.POST.get('status')
    #     remarks = request.POST.get('comments')
    
    #     pssport_verification.verification_status = verification_status
    #     pssport_verification.remarks = remarks
    #     pssport_verification.save()
    #     return redirect('dashboard_verifer')
    context ={
        # 'passport_application': passport_application,
        'passport_verification': pssport_verification
    }

    return render(request,'status_update.html', context)

def update_verifier_status(request, p_id):
    pssport_verification = PassportVerification.objects.get(id=p_id)
    if request.method == 'POST':
        verification_status = request.POST.get('status')
        remarks = request.POST.get('comments')
    
        pssport_verification.verification_status = verification_status
        pssport_verification.remarks = remarks
        pssport_verification.save()

        passport_apllication = pssport_verification.passport_application
        passport_apllication.application_status = verification_status
        passport_apllication.save()
        return redirect('dashboard_verifer')


def verifier_logout(request):
    del request.session['emp_id']

    return render(request,'index.html')
    # return redirect(login_view)  # Redirect to login page
