from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, StudentProfileForm, EmployerProfileForm
from .models import User

def landingpage(request):
    return render(request, 'core/landingpage.html')

def register(request):
    return render(request, 'core/register.html')

def student_account(request):
    return render(request, 'core/student_account.html')

def employer_account(request):
    return render(request, 'core/employer_account.html')

def login(request):
    return render(request, 'core/login.html')

def homepage(request):
    return render(request, 'core/homepage.html')

def searchpage(request):
    return render(request, 'core/searchpage.html')

def student_profile(request):
    return render(request, 'core/student_profile.html')

def edit_studentprofile(request):
    return render(request, 'core/edit_studentprofile.html')