from rest_framework.permissions import BasePermission, SAFE_METHODS


class CategoryPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # GET, HEAD, OPTIONS ruxsat etilgan
        return request.user and request.user.is_staff


class FoodItemPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated  # faqat login bo'lgan foydalanuvchilar yozishi mumkin


class OrderPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated  # Faqat login bo'lganlar GET qila oladi
        return request.user and request.user.is_authenticated
