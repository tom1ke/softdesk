from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorAndOrIsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return True if request.method in SAFE_METHODS else obj.author == request.user


class IsProjectAuthorAndIsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.project.author == request.user
