from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    message = 'Изменение чужого контента запрещено!'

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method not in permissions.SAFE_METHODS
                and obj.author == request.user
                or request.method in permissions.SAFE_METHODS)
