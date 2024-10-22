from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Проверка прав.
    Доступ только у авторизованного пользователя.
    Редактирование - только автор.
    """

    def has_permission(self, request, view):
        return (request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
