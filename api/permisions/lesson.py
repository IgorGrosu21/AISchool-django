from rest_framework import permissions
from rest_framework.views import Request

from api.models import User, Student, Homework, SpecificLesson, Lesson

class CanEditHomework(permissions.BasePermission):
  code = 'not_allowed_to_edit'
  message = 'Only the student himself can edit his homework.'
  
  def has_object_permission(self, request: Request, view, obj: Homework):
    if request.method in permissions.SAFE_METHODS:
      return True
    user: User = request.user.user
    if obj:
      return user in obj.allowed_to_edit
    student: Student = view.get_student()
    return student.user.id == user.id
  
class CanEditSpecificLesson(permissions.BasePermission):
  code = 'not_allowed_to_edit'
  message = 'Only lesson\'s teacher and klass managers can edit specific lesson.'
  
  def has_object_permission(self, request: Request, view, obj: SpecificLesson):
    if request.method in permissions.SAFE_METHODS:
      return True
    user: User = request.user.user
    if obj:
      return user in obj.allowed_to_edit
    lesson: Lesson = view.get_lesson()
    allowed_to_edit = {lesson.teacher.user.id} | set(lesson.klass.students.filter(is_manager=True).values_list('user__id'))
    return user.id in allowed_to_edit