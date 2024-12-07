from django.urls import path

from . import views

urlpatterns = [
    path("", views.landingpage, name="landingpage"),
    path('register/', views.register, name='register'),
    path('register/student/', views.student_account, name='student_account'),
    path('register/employer', views.employer_account, name='employer_account'),
    path('login/', views.login, name='login'),
]