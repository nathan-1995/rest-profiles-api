from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """"Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        # Safe methods are HTTP methods that do not modify the resource
        # (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # obj is the object that the user is trying to change
        # request.user is the user that is authenticated
        return obj.id == request.user.id
    
