
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name="base"),
    path('base' ,views.base, name="base"),
    path('SignUp', views.SignUp, name="SignUp"),
    path('doctor_login', views.doctor_login, name="doctor_login"),
    path('SignUpPatient', views.SignUpPatient, name="SignUpPatient"),
    path('patient_form', views.patient_form, name="patient_form"),
    path('About', views.About, name="About"),
    path('Contact', views.Contact, name="Contact"),
    path('Patient_Prescription', views.Patient_Prescription, name="Patient_Prescription"),
   
]