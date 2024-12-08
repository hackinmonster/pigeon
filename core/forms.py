from django import forms
from .models import StudentProfile, EmployerProfile
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email Address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['full_name', 'email', 'password']

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'company_email', 'company_password']
