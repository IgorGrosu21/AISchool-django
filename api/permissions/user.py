from rest_framework import permissions
from rest_framework.views import Request

from api.models import User

from .utils import is_authenticated_and_safe_readonly

class CanCreateUser(permissions.BasePermission):
  code = 'user_already_exists'
  message = 'User already exists.'

  @is_authenticated_and_safe_readonly
  def has_permission(self, request: Request, view):
    if request.method == 'POST':
      return not User.objects.filter(account=request.user).exists()
    return True