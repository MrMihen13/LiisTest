from rest_framework import permissions

from core.models import CustomUser


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.pk == request.user.pk


class IsAuthorUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.filter(id=request.user.id).first()
        return user.role == 'author'


class IsSubscriberUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.filter(id=request.user.id).first()
        return user.role == 'subscriber'
