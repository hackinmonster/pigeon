from django.urls import path

from . import views

urlpatterns = [
    path("", views.landingpage, name='landingpage'),
    path('register/', views.register, name='register'),
    path('register/student/', views.student_account, name='student_account'),
    path('register/employer', views.employer_account, name='employer_account'),
    path('login/', views.user_login, name='login'),
    path('home/', views.homepage, name='homepage'),
    path('search/', views.search_page, name='searchpage'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('employer_profile/', views.employer_profile, name='employer_profile'),
    path('apply/', views.apply, name='apply'),
    path('employer_application_view/', views.employer_application_view, name='employer_application_view'),
    path('edit_job_postings/', views.edit_job_postings, name='edit_job_postings'),
]