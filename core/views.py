from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, StudentProfileForm, EmployerProfileForm
from .models import User

def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            if user.is_student():
                student_profile_form = StudentProfileForm(request.POST)
                if student_profile_form.is_valid():
                    student_profile = student_profile_form.save(commit=False)
                    student_profile.user = user
                    student_profile.save()
            elif user.is_employer():
                employer_profile_form = EmployerProfileForm(request.POST)
                if employer_profile_form.is_valid():
                    employer_profile = employer_profile_form.save(commit=False)
                    employer_profile.user = user
                    employer_profile.save()

            return redirect('login')
        
    else:
        user_form = UserRegistrationForm()
        student_profile_form = StudentProfileForm()
        employer_profile_form = EmployerProfileForm()

    return render(request, 'core/register.html', {
        'user_form': user_form,
        'student_profile_form': student_profile_form,
        'employer_profile_form': employer_profile_form,
    })
