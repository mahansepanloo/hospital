from rest_framework.permissions import BasePermission
from accounts.models import Nurse

class IsNurse(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_nurse and request.user.is_authenticated
