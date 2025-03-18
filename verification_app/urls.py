
from django.contrib import admin
from django.urls import path
from verification_app import views
from django.conf import settings
from django.conf.urls.static import static


from verification_app.views import logout_view
urlpatterns = [
<<<<<<< Updated upstream
    path('register/', views.register_employee, name='register'),
    path('login_verifer/',views.login_view,name='login_verifer'),
    path('login_verifer_method/',views.login_verifer_method,name='login_verifer_method'),
    path('dashboard_verifer/',views.dashboard_verifier_view,name='dashboard_verifer'),
    path('status_update/<int:p_id>/',views.status_update_view,name='status_update'),
    path('update_verifier_status/<int:p_id>/',views.update_verifier_status,name='update_verifier_status'),
=======
 path('register/', views.register_employee, name='register'),
 path('login_verifer/',views.login_view,name='login_verifer'),
 path('login_verifer_method/',views.login_verifer_method,name='login_verifer_method'),
 path('dashboard_verifer/',views.dashboard_verifier_view,name='dashboard_verifer'),
 path('status_update/',views.status_update_view,name='status_update'),
 path('logout/', views.logout_view, name='logout_views'),
>>>>>>> Stashed changes

    path('verifier_logout/',views.verifier_logout,name='verifier_logout'),

   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 