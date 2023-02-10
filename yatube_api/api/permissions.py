from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Нет доступа к изменению контента!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.author == request.user
