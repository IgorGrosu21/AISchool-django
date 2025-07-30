from rest_framework import permissions
from rest_framework.views import Request

from api.models import User, School, Klass

class CanEditSchool(permissions.BasePermission):
  code = 'not_allowed_to_edit'
  message = 'Only school managers can edit school.'
  
  def has_object_permission(self, request: Request, view, obj: School):
    if request.method in permissions.SAFE_METHODS:
      return True
    user: User = request.user.user
    return user in obj.allowed_to_edit

class CanEditKlass(permissions.BasePermission):
  code = 'not_allowed_to_edit'
  message = 'Only school managers and klass teacher can edit klass.'
  
  def has_object_permission(self, request: Request, view, obj: Klass):
    if request.method in permissions.SAFE_METHODS:
      return True
    user: User = request.user.user
    return user in obj.allowed_to_edit