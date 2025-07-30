from ...name import UserNameSerializer

class UserSerializer(UserNameSerializer):
  class Meta(UserNameSerializer.Meta):
    fields = UserNameSerializer.Meta.fields + ['avatar', 'is_verified']