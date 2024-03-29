from rest_framework import BasePermission

class Is_staff(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff and request.user.is_authenticated

class Is_superuser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser and request.user.is_authenticated
