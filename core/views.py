from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import StudentProfileForm, EmployerProfileForm, CustomAuthenticationForm
from .models import User, StudentProfile, EmployerProfile

def landingpage(request):
    return render(request, 'core/landingpage.html')

def register(request):
    if request.method == 'POST':
        account_type = request.POST.get('account_type')
        
        if account_type == 'student':
            student_form = StudentProfileForm(request.POST)
            if student_form.is_valid():
                user = User.objects.create_user(
                    username=student_form.cleaned_data['email'],
                    password=student_form.cleaned_data['password'],
                    user_type='student'
                )
                student_profile = student_form.save(commit=False)
                student_profile.user = user
                student_profile.save()

                return redirect('homepage')
            else:
                return render(request, 'core/register.html', {'student_form': student_form, 'employer_form': EmployerProfileForm()})
        
        elif account_type == 'employer':
            employer_form = EmployerProfileForm(request.POST)
            if employer_form.is_valid():
                user = User.objects.create_user(
                    username=employer_form.cleaned_data['company_email'],
                    password=employer_form.cleaned_data['company_password'],
                    user_type='employer'
                )
                employer_profile = employer_form.save(commit=False)
                employer_profile.user = user
                employer_profile.save()

                return redirect('homepage')
            else:
                return render(request, 'core/register.html', {'student_form': StudentProfileForm(), 'employer_form': employer_form})
        
        else:
            return HttpResponse("Invalid form submission.")
    
    else:
        student_form = StudentProfileForm()
        employer_form = EmployerProfileForm()
        return render(request, 'core/register.html', {'student_form': student_form, 'employer_form': employer_form})

def student_account(request):
    return render(request, 'core/student_account.html')

def employer_account(request):
    return render(request, 'core/employer_account.html')

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            remember_me = request.POST.get('remember_me', False)
            if remember_me:
                request.session.set_expiry(1209600)  #set session expiry to 2 weeks
            return redirect('homepage')
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'core/login.html', {'form': form})
    else:
        form = CustomAuthenticationForm()
        return render(request, 'core/login.html', {'form': form})

def homepage(request):
    user = request.user
    if user.is_student():
        profile_url = 'student_profile'
    elif user.is_employer():
        profile_url = 'employer_profile'
    else:
        profile_url = None

    return render(request, 'core/homepage.html', {
        'profile_url': profile_url,
    })

def search_page(request):
    job_title = request.GET.get('job_title', '')
    location = request.GET.get('location', '')

    return render(request, 'core/searchpage.html', {
        'job_title': job_title,
        'location': location,
    })

def student_profile(request):
    return render(request, 'core/student_profile.html')

def edit_profile(request):
    return render(request, 'core/edit_profile.html')

def employer_profile(request):
    return render(request, 'core/employer_profile.html')

def apply(request):
    return render(request, 'core/apply.html')

def employer_application_view(request):
    return render(request, 'core/employer_application_view.html')

def edit_job_postings(request):
    return render(request, 'core/edit_job_postings.html')