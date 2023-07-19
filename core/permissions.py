from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsCurrentUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        print("obj", obj.user)
        print("user", request.user)
        return bool(obj.user == request.user)
