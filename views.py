from django.shortcuts import render
from .forms import DoctorSignUp,PatientSignUp,PatientInfo
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def base(request):
    return render(request, 'base.html',{})


def SignUp(request):
 if request.method=="POST":
   form= DoctorSignUp(request.POST or None)
   if form.is_valid():
        form.save()
        return render(request, 'doctor_login.html',{})
          

 else:
  return render(request, 'SignUp.html',{})



def doctor_login(request):
   return render(request, 'doctor_login.html',{})


def SignUpPatient(request):
 if request.method=="POST":
   form= PatientSignUp(request.POST or None)
   if form.is_valid():
        form.save()
        return render(request, 'patient_form.html',{})
          

 else:
  return render(request, 'SignUpPatient.html',{})
 

def patient_form(request):
  if request.method=="POST":
   form= PatientInfo(request.POST, request.FILES )
   if form.is_valid():
        form.save()
        return render(request, 'patient_form.html',{})
          

  else:
   return render(request, 'patient_form.html',{})


def About(request):
   return render(request, 'About.html',{})

def Contact(request):
   return render(request, 'Contact.html',{})

def Patient_Prescription(request):
   return render(request, 'Patient_Prescription.html',{})
