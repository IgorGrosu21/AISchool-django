from rest_framework import generics
from rest_framework.request import Request
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from drf_spectacular.utils import extend_schema
from django.db.models.manager import BaseManager

from api.permissions import CanCreateUser
from api.models import User, Person, Parent, Student, Teacher
from api.serializers import DetailedUserSerializer, UserRoutesSerializer

from ..media import MediaView

USER_TYPE_MAPPING: dict[str, BaseManager[Person]] = {
  'parent': Parent.objects,
  'student': Student.objects,
  'teacher': Teacher.objects
}
    
@extend_schema(tags=['api / user'])
class DetailedUserView(RetrieveModelMixin, CreateModelMixin, MediaView):
  queryset = User.objects.all()
  serializer_class = DetailedUserSerializer
  media_field = 'avatar'
  permission_classes = [CanCreateUser]
  
  def get_object(self) -> User:
    return self.request.user.user
  
  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def post(self, request: Request, *args, **kwargs):
    request.data.pop('id')
    return self.create(request, *args, **kwargs)

  def perform_create(self, serializer: DetailedUserSerializer):
    user_type = self.request.data.pop('user_type')
    user = serializer.save(account=self.request.user)
    manager = USER_TYPE_MAPPING[user_type]
    if not manager.filter(user=user).exists():
      manager.create(user=user)

@extend_schema(tags=['api / user'])
class UserRoutesView(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserRoutesSerializer
  
  def get_object(self) -> User:
    return self.request.user.user