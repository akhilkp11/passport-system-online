
from django.views.generic import TemplateView,FormView
from django.views import View
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from passport_app.forms import PassportOfficerForm,VerificationOfficerForm
from passport_app.models import PassportOfficer,PassportVerifier
from django.views.generic import TemplateView,View,UpdateView
from .forms import AdminLoginForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



class IndexPageView(View):
    template_name = "index.html"
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name) 
    

class AdminLogin(View):
    template_name='AdminLogin.html'
    form_class=AdminLoginForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_instance=self.form_class(request.POST)
        if form_instance.is_valid():
            uname=form_instance.cleaned_data.get("username")
            pwd=form_instance.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                return redirect("home")
        return render(request,self.template_name,{"form":form_instance})
    


class AdminLogout(View):
    def post(self,request,*args,**kwargs):
        logout(request)
        return redirect("admin-login")



class HomeView(TemplateView):
    template_name = "home.html"




class AddPassportOfficerView(View):
    template_name = "admin/add_passportofficer.html"

    def get(self, request):
        form = PassportOfficerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print("Received POST Data:", request.POST.dict())  # Debugging
        form = PassportOfficerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Passport Officer added successfully!")
            return redirect("list-passportofficer")  # Redirect to avoid duplicate submissions
        else:
            print("Form Errors:", form.errors)  # Debugging
        return render(request, self.template_name, {'form': form})
    
class ListPassportofficerView(View):
    template_name = "admin/list_And_Manage_passportofficer.html"

    def get(self, request, *args, **kwargs):
        qs = PassportOfficer.objects.all()
        return render(request, self.template_name, {"data": qs})
    
    

class ListPassportofficerView(View):
    template_name="admin/list_And_Manage_passportofficer.html"
    def get(self,request,*args,**kwargs):
        qs=PassportOfficer.objects.all()
        return render(request,self.template_name,{"data":qs})
 


class PassportOfficerUpdateView(UpdateView):
    model = PassportOfficer
    template_name = 'admin/updateofficer.html'  
    fields = ['name', 'email', 'employee_id', 'phone_number', 'branch_location', 'assigned_region', 'date_of_joining', 'status']  
    context_object_name = 'passport_officer'  
    
    def get_object(self, queryset=None):
        officer_id = self.kwargs.get('id')  
        return get_object_or_404(PassportOfficer, id=officer_id)
    
    def get_success_url(self):
        
        return reverse_lazy('list-passportofficer') 


class DeletePassportOfficerView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=PassportOfficer.objects.get(id=id).delete()
        return redirect("list-passportofficer")
    



class AddVerificationOfficerView(View):
    template_name = "admin/add_verificationofficer.html"

    def get(self, request):
        form = VerificationOfficerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print("Received POST Data:", request.POST.dict())  # Debugging
        form = VerificationOfficerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Passport Officer added successfully!")
            return redirect("list-verificationofficer")  
        else:
            print("Form Errors:", form.errors)  # Debugging
        return render(request, self.template_name, {'form': form})
    
class ListverificationOfficer(View):
    template_name="admin/list_verificationofficer.html"
    def get(self,request,*args,**kwargs):
        qs=PassportVerifier.objects.all()
        return render(request,self.template_name,{"data":qs})
    

from user_app.models import PassportApplication

def ListManagePassport_application(request):
    data = PassportApplication.objects.all()
    return render(request, "admin/List_and_Update_passportapplication.html",{"data": data})