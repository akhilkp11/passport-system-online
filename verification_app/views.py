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
        print('status updated')


        passport_apllication = pssport_verification.passport_application
        passport_apllication.application_status = verification_status
        passport_apllication.save()
        return redirect('dashboard_verifer')


def verifier_logout(request):
    del request.session['emp_id']
    return render(request,'index.html')
    # return redirect(login_view)  # Redirect to login page

    return render(request,'index.html')
    # return redirect(login_view)  # Redirect to login page

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import FormView, TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.conf import settings
from smtplib import SMTPException
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string

UserModel = get_user_model()

def send_email(customer_email, password_reset_link):
    subject = "Password Reset Request"
    message = f"""Dear Customer,

You requested a password reset. Click the link below to reset your password:

{password_reset_link}

If you did not request a password reset, please ignore this email.

Thank you for choosing us!
"""
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [customer_email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        print(f"Email successfully sent to {customer_email}")
    except SMTPException as e:
        print(f"Error sending email to {customer_email}: {e}")


class PasswordResetView(FormView):
    template_name = "password_reset.html"
    success_url = reverse_lazy("password_reset_done")
    form_class = PasswordResetForm

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        try:
            user = UserModel.objects.get(email=email)
            token_generator = default_token_generator
            token = token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            password_reset_link = f"http://127.0.0.1:8000/password_reset_confirm/{uid}/{token}/"

            # Send the email with the reset link
            send_email(email, password_reset_link)
        except UserModel.DoesNotExist:
            pass  # Prevent revealing that the email is invalid

        return super().form_valid(form)


class PasswordResetDoneView(TemplateView):
    template_name = "password_reset_done.html"


class PasswordResetConfirmView(FormView):
    template_name = "password_reset_confirm.html"
    form_class = SetPasswordForm
    success_url = reverse_lazy("password_reset_complete")
    token_generator = default_token_generator

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        self.user = self.get_user(kwargs['uidb64'])
        self.validlink = False
        if self.user is not None and self.token_generator.check_token(self.user, kwargs['token']):
            self.validlink = True
            return super().dispatch(*args, **kwargs)
        return self.render_to_response(self.get_context_data())

    def get_user(self, uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            return UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            return None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.user  # Important! Pass the user to the form
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PasswordResetCompleteView(TemplateView):
    template_name = "password_reset_complete.html"
