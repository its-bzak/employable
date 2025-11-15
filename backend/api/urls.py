from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileViewSet,
    CompanyProfileViewSet,
    ApplicationViewSet,
    EducationViewSet,
    WorkExperienceViewSet,
    JobViewSet
)

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'companyprofiles', CompanyProfileViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'jobpostings', JobViewSet)
router.register(r'education', EducationViewSet)
router.register(r'workexperience', WorkExperienceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]