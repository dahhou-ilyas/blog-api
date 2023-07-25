from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS requests (read-only) to all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow POST (user creation) only to admin users
        return request.user.is_superuser