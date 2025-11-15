from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if hasattr(obj, 'user'):
            return obj.user == request.user
        if hasattr(obj, 'company_name'):
            return obj.company_name == request.user
        if hasattr(obj, 'company'):
            return obj.company.company_name == request.user
        if hasattr(obj, 'user_profile'):
            return obj.user_profile.user == request.user

        return False

class IsCompanyProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'is_company_profile', None)

class IsUserProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'is_user_profile', None)