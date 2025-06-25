from functools import wraps

from rest_framework.serializers import ModelSerializer, UUIDField, SerializerMethodField

from api.models import User

class UserNameSerializer(ModelSerializer):
  id = UUIDField()
  profile_link = SerializerMethodField()
  
  def handle_staff(func):
    @wraps(func)
    def wrapped(self, obj: User):
      if obj.account.is_staff:
        return None
      return func(self, obj)
    return wrapped
  
  @handle_staff
  def get_profile_link(self, obj: User):
    return f'teachers/{obj.teacher.id}' if obj.is_teacher else f'students/{obj.student.id}'
  
  class Meta:
    fields = ['id', 'name', 'surname', 'profile_link']
    model = User