from rest_framework.serializers import SerializerMethodField

from api.models import User, Media

from ...name import UserNameSerializer

class UserSerializer(UserNameSerializer):
  avatar = SerializerMethodField()
  
  def get_avatar(self, obj: User):
    if obj.avatar:
      return Media.append_prefix(obj.avatar)
  
  class Meta(UserNameSerializer.Meta):
    fields = UserNameSerializer.Meta.fields + ['avatar', 'is_verified']