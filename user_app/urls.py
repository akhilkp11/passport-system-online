
from django.contrib import admin
from django.urls import path,include
from user_app import views
urlpatterns = [
 path('register_user/',views.registrationview,name='register_user'),
 path('login/',views.loginview,name='login'),
 path('logout/', views.logoutview, name='logout'),
 path('dashboard/',views.dashboard_view,name='dashboard'),
 path('application_form/', views.application_form_view, name='application_form'),

  path('payment/<int:application_id>/', views.payment_page, name='payment_page'),
    path('payment_method/<int:application_id>/', views.payment_method, name='payment_method'),
    path('payment_status/', views.payment_callback, name='payment_callback'),
    path('application_detail/<int:application_id>/', views.application_detail, name='application_detail'),
    path('track/', views.track_service_request, name='track_service_request'),
      path('logout/', views.user_logout, name='logout'),
    
    



    

]
 