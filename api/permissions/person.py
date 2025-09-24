from rest_framework import permissions
from rest_framework.views import Request

from api.models import User, Person

from .utils import is_authenticated, is_authenticated_and_safe_readonly

class IsSelf(permissions.BasePermission):
  code = 'private_view'
  message = 'Only the user himself can access this info.'

  @is_authenticated
  def has_object_permission(self, request: Request, view, obj: Person):
    user: User = request.user.user
    return user.id == obj.user.id

class IsSelfOrReadonly(permissions.BasePermission):
  code = 'private_edit'
  message = 'Only the user himself can edit this info.'

  @is_authenticated_and_safe_readonly
  def has_object_permission(self, request: Request, view, obj: Person):
    user: User = request.user.user
    return user.id == obj.user.id

class IsParent(permissions.BasePermission):
  code = 'parent_view'
  message = 'Only the parent can access this info.'

  @is_authenticated
  def has_permission(self, request: Request, view):
    user: User = request.user.user
    return user.is_parent

class IsParentOrReadonly(permissions.BasePermission):
  code = 'parent_edit'
  message = 'Only the parent can edit this info.'

  @is_authenticated_and_safe_readonly
  def has_permission(self, request: Request, view):
    user: User = request.user.user
    return user.is_parent

class IsStudent(permissions.BasePermission):
  code = 'student_view'
  message = 'Only the student can access this info.'

  @is_authenticated
  def has_permission(self, request: Request, view):
    user: User = request.user.user
    return user.is_student

class IsStudentOrReadonly(permissions.BasePermission):
  code = 'student_edit'
  message = 'Only the student can edit this info.'

  @is_authenticated_and_safe_readonly
  def has_permission(self, request: Request, view):
    user: User = request.user.user
    return user.is_student

class IsKlassManager(permissions.BasePermission):
  code = 'klass_manager_view'
  message = 'Only the klass manager can access this info.'

  @is_authenticated
  def has_permission(self, request: Request, view):
    user: User = request.user.user
    if not user.is_student:
      return False
    return user.student.is_manager

class IsKlassManagerOrReadonly(permissions.BasePermission):
  code = 'klass_manager_edit'
  message = 'Only the klass manager can edit this info.'

  @is_authenticated_and_safe_readonly
  def has_permission(self, request: Request, view):
    user: User = request.user.user
    if not user.is_student:
      return False
    return user.student.is_manager

class IsTeacher(permissions.BasePermission):
  code = 'teacher_view'
  message = 'Only the teacher can access this info.'

  @is_authenticated
  def has_permission(self, request: Request, view):
    user: User = request.user.user
    return user.is_teacher

class IsTeacherOrReadonly(permissions.BasePermission):
  code = 'teacher_edit'
  message = 'Only the teacher can edit this info.'

  @is_authenticated_and_safe_readonly
  def has_permission(self, request: Request, view):
    user: User = request.user.user
    return user.is_teacher

class IsSchoolManager(permissions.BasePermission):
  code = 'school_manager_view'
  message = 'Only the school manager can access this info.'

  @is_authenticated
  def has_permission(self, request: Request, view):
    user: User = request.user.user
    if not user.is_teacher:
      return False
    return user.teacher.is_manager

class IsSchoolManagerOrReadonly(permissions.BasePermission):
  code = 'school_manager_edit'
  message = 'Only the school manager can edit this info.'

  @is_authenticated_and_safe_readonly
  def has_permission(self, request: Request, view):
    user: User = request.user.user
    if not user.is_teacher:
      return False
    return user.teacher.is_manager