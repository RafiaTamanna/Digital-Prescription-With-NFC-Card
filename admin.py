from django.contrib import admin
from .models import SignUp,SignUpPatient,PatientDetails

# Register your models here.
admin.site.register(SignUp)
admin.site.register(SignUpPatient)
admin.site.register(PatientDetails)
