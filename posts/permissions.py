from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # Read-only permission are allowed for any one
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permission only allowed for post author
        obj.author == request.user
