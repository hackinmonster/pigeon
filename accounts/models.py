from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('employer', 'Employer'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def is_student(self):
        return self.user.type == 'student'
    
    def is_employer(self):
        return self.user.type == 'employer'
    
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, default='Unknown')
    school = models.CharField(max_length=100)

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)