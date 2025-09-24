from functools import wraps

from rest_framework import permissions
from rest_framework.views import Request

def is_authenticated(func):
  @wraps(func)
  def wrapped(self: permissions.BasePermission, request: Request, *args, **kwargs):
    if request.user == None or request.user.is_anonymous:
      return False
    return func(self, request, *args, **kwargs)

  return wrapped

def is_authenticated_and_safe_readonly(func):
  @wraps(func)
  def wrapped(self: permissions.BasePermission, request: Request, *args, **kwargs):
    if request.user == None or request.user.is_anonymous:
      return False
    if request.method in permissions.SAFE_METHODS:
      return True
    return func(self, request, *args, **kwargs)

  return wrapped