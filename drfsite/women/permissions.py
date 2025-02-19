from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    IsAdminOrReadOnly - класс пермишн для предоставления прав удаления записей, и чтение для всех
    первая проверка в теле - если это безопасный запрос ('GET', 'HEAD', 'OPTIONS')
        return предоставить доступ (так мы даём доступ для чтения всем)
    """
    def has_permission(self, request, view):
        """
        has_permission - метод из BasePermission, в нём определяется логика для предоставления прав на все записи
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        # если пользователь из запроса, в таблице, находится в поле is_staff (администратор)
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    IsOwnerOrReadOnly - класс пермишн для предоставления прав изменения только для автора записи, и чтение для всех
    """

    def has_object_permission(self, request, view, obj):
        """
        has_object_permission - метод из BasePermission, в нём определяется логика для предоставления прав на конекретный объект
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        # поле user данного объекта в таблице совпадает с юзером в реквесте
        return obj.user == request.user