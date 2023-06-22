from django import forms
from .models import SignUp,SignUpPatient,PatientDetails


class DoctorSignUp(forms.ModelForm):
    class Meta:
        model= SignUp
        fields=['fname','lname','email','password','checkbox']

class PatientSignUp(forms.ModelForm):
    class Meta:
        model= SignUpPatient
        fields=['fname','lname','email','password','checkbox']


class PatientInfo(forms.ModelForm):
    class Meta:
        model= PatientDetails
        fields=['fullname','email','phone','age','height','weight','blood','medhistory','meddetails','healthcond','presimage']


