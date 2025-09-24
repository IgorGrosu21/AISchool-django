from rest_framework import generics
from drf_spectacular.utils import extend_schema

from api.models import User
from api.permissions import IsSelf
from api.serializers import ParentHomeSerializer, StudentHomeSerializer, TeacherHomeSerializer

from .parent_with_data import parent_with_data
from .student_with_data import student_with_data
from .teacher_with_data import teacher_with_data

@extend_schema(tags=['api / person'])
class PersonHomeView(generics.RetrieveAPIView):
  permission_classes = [IsSelf]

  def get_object(self):
    user: User = self.request.user.user
    user_type = user.account_type
    person = user.person
    if user_type == 'parent':
      return parent_with_data(person)
    if user_type == 'student':
      return student_with_data(person)
    if user_type == 'teacher':
      return teacher_with_data(person)
    return person

  def get_serializer_class(self):
    if self.request.user.is_anonymous:
      return ParentHomeSerializer

    user_type = self.request.user.user.account_type
    if user_type == 'student':
      return StudentHomeSerializer
    if user_type == 'teacher':
      return TeacherHomeSerializer
    return ParentHomeSerializer