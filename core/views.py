from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, StudentProfileForm, EmployerProfileForm
from .models import User

def home(request):
    return render(request, 'core/home.html')

def register(request):
    return render(request, 'core/register.html')

def student_account(request):
    return render(request, 'core/student_account.html')

def employer_account(request):
    return render(request, 'core/employer_account.html')

def login(request):
    return render(request, 'core/login.html')