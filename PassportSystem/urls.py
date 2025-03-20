
from django.contrib import admin
from django.urls import path,include
from passport_app import views
from passport_app.views import PassportOfficerUpdateView 
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('passport_app.urls')),
    path("",views.IndexPageView.as_view(), name="index"),
    path('home/', views.HomeView.as_view(), name='home'),
    path('admin-login/',views.AdminLogin.as_view(),name='admin-login'),
    path('admin-logout/',views.AdminLogout.as_view(),name='admin-logout'),
    path('add_passportofficer/',views.AddPassportOfficerView.as_view(),name='add-passportofficer'),
    path('list_passportofficer/', views.ListPassportofficerView.as_view(), name='list-passportofficer'),
    path('update-passportofficer/<int:id>/',PassportOfficerUpdateView.as_view(), name='update-passportofficer'),
    path('delete_passportofficer/<int:pk>/',views.DeletePassportOfficerView.as_view(),name='delete-passportofficer'),

    path('add_passportverifier/',views.AddVerificationOfficerView.as_view(),name='add-verificationofficer'),
    # path('list_verificationofficer/', views.ListverificationOfficer.as_view(), name='list-verificationofficer'),


    path('list_verificationofficer/', views.list_verificationofficer, name='list_verificationofficer'),


      path('ListManagePassport_application/', views.ListManagePassport_application, name='ListManagePassport_application'),
      path('view_passport_application/<int:pasport_id>/', views.view_passport_application, name='view_passport_application'),
      path('save_passport_application/', views.save_passport_application, name='save_passport_application'),
      path('admin_update_passport_status/<int:p_id>/', views.admin_update_passport_status, name='admin_update_passport_status'),
    





    path('user/',include('user_app.urls')),
    path('verification/', include('verification_app.urls')), 







    # path('add-officer/', views.AddPassportOfficerView.as_view(), name='add_officer'),
]
