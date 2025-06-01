from rest_framework.serializers import ModelSerializer, UUIDField

from api.models import User, Media

class UserSerializer(ModelSerializer):
  id = UUIDField()
  
  class Meta:
    fields = ['id', 'is_teacher', 'name', 'surname', 'avatar', 'student', 'teacher']
    model = User
    extra_kwargs = {
      'avatar': {'read_only': True, 'required': False, 'allow_null': True},
      'student': {'read_only': True},
      'teacher': {'read_only': True}
    }
    
  def to_representation(self, instance):
    r = super().to_representation(instance)
    if instance.avatar:
      r['avatar'] = Media.append_prefix(instance.avatar)
    r['profile_link'] = f'teachers/{instance.teacher.id}' if instance.is_teacher else f'students/{instance.student.id}'
    return r