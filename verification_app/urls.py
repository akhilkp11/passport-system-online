from django.contrib import admin
from django.urls import path
from verification_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views






urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_employee, name='register'),
    path('login_verifer/',views.login_view,name='login_verifer'),
    path('login_verifer_method/',views.login_verifer_method,name='login_verifer_method'),
    path('dashboard_verifer/',views.dashboard_verifier_view,name='dashboard_verifer'),
    path('status_update/<int:p_id>/',views.status_update_view,name='status_update'),
    path('update_verifier_status/<int:p_id>/',views.update_verifier_status,name='update_verifier_status'),

    path('verifier_logout/',views.verifier_logout,name='verifier_logout'),

   


    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<str:uidb64>/<str:token>/', views.reset_password, name='reset_password'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

