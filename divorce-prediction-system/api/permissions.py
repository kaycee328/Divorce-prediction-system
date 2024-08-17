from rest_framework.permissions import BasePermission


class IsAdminOrUser(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_staff:
                return True
            return request.method in [
                "GET",
                "HEAD",
                "OPTIONS",
            ]  # Allow read-only for non-admin users
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user
