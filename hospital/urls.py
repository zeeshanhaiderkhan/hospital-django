from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.index, name= 'index'),
    path('home/', views.index, name= 'index'),

##admin
    path('patient/', views.patient, name= 'patient'),
    path('adminbase/', views.adminbase, name= 'adminbase'),
    path('admin-dashboard/', views.admin_dashboard, name= 'admin_dashboard'),


##doctor
    path('doctorsignup/', views.doctor_signup, name= 'doctor_sign_up'),
    path('doctorlogin/', views.doctor_login, name='doctor_login'),
    path('doctorclick/', views.doctorclick, name='doctorclick'),
    path('doctorbase/', views.doctorbase, name='doctorbase'),
    path('doctordashboard/', views.doctordashboard, name='doctordashboard'),
    path('doctor_main/', views.doctordashboard, name='doctor_main'),
    path('doctor_patient/', views.doctor_patient, name='doctor_patient'),
    path('doctor_view_patient/', views.doctor_view_patient, name='doctor_view_patient'),
    path('doctor_view_patient/doctor_view_patient_report/',views.doctor_view_patient_report,name='doctor_view_patient_report'),
    path('doctor_view_reports/', views.doctor_view_reports, name='doctor_view_reports'),
    path('doctor_notifications/', views.doctor_notifications, name='doctor_notifications'),
    path('/', views.LogOut, name='logout'),
    path('afterlogin/', views.afterlogin_view,name='afterlogin'),
    path('doctorlogin/afterlogin/', views.afterlogin_view,name='afterlogin'),

    #patient
    path('patientsignup/', views.patient_signup, name= 'patient_sign_up'),
    path('patientlogin/', views.patient_login, name='patient_login'),
    path('patientclick/', views.patientclick, name='patientclick'),
    path('patientbase/', views.patientbase, name='patientbase'),
    path('patientdashboard/', views.patient_dashboard, name= 'patient_dashboard'),
    path('patient_report/', views.patient_report, name= 'patient_report'),
    path('patient_view_reports/', views.patient_view_reports, name='patient_view_reports'),
    path('patient_upload_report/', views.patient_upload_report, name='patient_upload_report'),
    path('patientlogin/afterlogin/', views.afterlogin_view,name='afterlogin'),
    
]