from django.urls import path

from . import views

urlpatterns = [
    path("", views.landingpage, name='landingpage'),
    path('register/', views.register, name='register'),
    path('register/student/', views.student_account, name='student_account'),
    path('register/employer', views.employer_account, name='employer_account'),
    path('login/', views.user_login, name='login'),
    path('home/', views.homepage, name='homepage'),
    path('search/', views.searchpage, name='searchpage'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('edit_student_profile/', views.edit_student_profile, name='edit_student_profile'),
    path('employer_profile/', views.employer_profile, name='employer_profile'),
    path('edit_employer_profile/', views.edit_employer_profile, name='edit_employer_profile'),
]