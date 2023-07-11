from rest_framework.permissions import BasePermission
from account.models import Member

class IsWriterOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.writer == request.member