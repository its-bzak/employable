from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, unique=True)
    extra_url = models.URLField(blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)

    def __str__(self):
        return self.user.username

class CompanyProfile(models.Model):
    company_name = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    industry = models.URLField(blank=True)

    def __str__(self):
        return self.company_name.username



class Application(models.Model):

    STATUS_OPTIONS = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    position_title = models.CharField(max_length=255)
    position_description = models.CharField(max_length=1000)
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_OPTIONS, default='pending')
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.position_title}"

class Education(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

class WorkExperience(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)