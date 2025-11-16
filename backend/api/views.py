from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly, IsCompanyProfile, IsUserProfile
from .models import UserProfile, CompanyProfile, Application, Education, WorkExperience, JobPosting
from .serializers import (
    UserProfileSerializer,
    RegisterSerializer,
    CompanyProfileSerializer,
    ApplicationSerializer,
    EducationSerializer,
    WorkExperienceSerializer, JobPostingSerializer
)
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class RegisterView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = RegisterSerializer

class CompanyProfileViewSet(viewsets.ModelViewSet):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
