from api.models import User

from ..._helpers import CreatableSerializer

class UserNameSerializer(CreatableSerializer):
  class Meta:
    fields = ['id', 'name', 'surname', 'profile_link']
    model = User