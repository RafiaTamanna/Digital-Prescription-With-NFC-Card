from django.db import models
from django import forms

# Create your models here.



    
# GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('?', 'Prefer not to say'),
#     )




class SignUp(models.Model):
    fname= models.CharField(max_length=220)
    lname= models.CharField(max_length=220)
    email= models.EmailField(max_length=254)
    password= models.CharField(max_length=220)
    
    # CHOICES = [('M','Male'),('F','Female'), ('O','Other')]
    # Gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    checkbox= models.BooleanField()


    def __str__(self):
        return self.fname + ' '+ self.lname



class SignUpPatient(models.Model):
    fname= models.CharField(max_length=220)
    lname= models.CharField(max_length=220)
    email= models.EmailField(max_length=254)
    password= models.CharField(max_length=220)
    
    # CHOICES = [('M','Male'),('F','Female'), ('O','Other')]
    # Gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    checkbox= models.BooleanField()


    def __str__(self):
        return self.fname + ' '+ self.lname
    

class PatientDetails(models.Model):
    fullname= models.CharField(max_length=220)
    email= models.EmailField(max_length=220)
    phone= models.IntegerField()
    age= models.IntegerField()
    height= models.FloatField()
    weight= models.FloatField()
    blood= models.CharField(max_length=220)
    medhistory= models.CharField(max_length=1000)
    meddetails= models.CharField(max_length=1000)
    healthcond= models.CharField(max_length=1000)
    #gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    presimage= models.FileField(null=True, blank=True, upload_to="images/" )

    def __str__(self):
        return 'Info of: '+ self.fullname





