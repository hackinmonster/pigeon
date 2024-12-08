from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import StudentProfileForm, EmployerProfileForm, CustomAuthenticationForm
from .models import User

def landingpage(request):
    return render(request, 'core/landingpage.html')

def register(request):
    if request.method == 'POST':
        account_type = request.POST.get('account_type')
        
        if account_type == 'student':
            student_form = StudentProfileForm(request.POST)
            if student_form.is_valid():
                # Create User for student
                user = User.objects.create_user(
                    username=student_form.cleaned_data['email'],  # You can customize the username logic
                    password=student_form.cleaned_data['password'],
                    user_type='student'  # Set the account type to 'student'
                )
                # Save Student Profile
                student_profile = student_form.save(commit=False)
                student_profile.user = user  # Link user to profile
                student_profile.save()

                return redirect('homepage')  # Redirect to homepage on success
            else:
                return render(request, 'core/register.html', {'student_form': student_form, 'employer_form': EmployerProfileForm()})
        
        elif account_type == 'employer':
            employer_form = EmployerProfileForm(request.POST)
            if employer_form.is_valid():
                # Create User for employer
                user = User.objects.create_user(
                    username=employer_form.cleaned_data['company_email'],  # You can customize the username logic
                    password=employer_form.cleaned_data['company_password'],
                    user_type='employer'  # Set the account type to 'employer'
                )
                # Save Employer Profile
                employer_profile = employer_form.save(commit=False)
                employer_profile.user = user  # Link user to profile
                employer_profile.save()

                return redirect('homepage')  # Redirect to homepage on success
            else:
                return render(request, 'core/register.html', {'student_form': StudentProfileForm(), 'employer_form': employer_form})
        
        else:
            return HttpResponse("Invalid form submission.")
    
    else:
        # For GET request, just render the empty forms
        student_form = StudentProfileForm()
        employer_form = EmployerProfileForm()
        return render(request, 'core/register.html', {'student_form': student_form, 'employer_form': employer_form})

def student_account(request):
    return render(request, 'core/student_account.html')

def employer_account(request):
    return render(request, 'core/employer_account.html')

def user_login(request):  # Renamed view function to avoid conflict
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Log the user in using the correct import
            remember_me = request.POST.get('remember_me', False)
            if remember_me:
                request.session.set_expiry(1209600)  # Set session expiry to 2 weeks
            return redirect('homepage')  # Redirect to homepage after successful login
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'core/login.html', {'form': form})
    else:
        form = CustomAuthenticationForm()
        return render(request, 'core/login.html', {'form': form})

def homepage(request):
    return render(request, 'core/homepage.html')

def searchpage(request):
    return render(request, 'core/searchpage.html')

def student_profile(request):
    return render(request, 'core/student_profile.html')

def edit_profile(request):
    return render(request, 'core/edit_profile.html')

def employer_profile(request):
    return render(request, 'core/employer_profile.html')