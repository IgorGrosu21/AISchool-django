from rest_framework import generics
from drf_spectacular.utils import extend_schema

from api.permissions import IsSelf
from api.serializers import ParentHomeSerializer, StudentHomeSerializer, TeacherHomeSerializer

@extend_schema(tags=['api / person'])
class PersonHomeView(generics.RetrieveAPIView):
  permission_classes = [IsSelf]
  
  def get_object(self):
    return self.request.user.user.person
  
  def get_serializer_class(self):
    if self.request.user.is_anonymous:
      return ParentHomeSerializer
    
    user_type = self.request.user.user.account_type
    if user_type == 'student':
      return StudentHomeSerializer
    elif user_type == 'teacher':
      return TeacherHomeSerializer
    return ParentHomeSerializer