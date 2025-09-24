from ..user import UserNameSerializer

from ..._helpers import RetrieveableSerializer

class PersonNameSerializer(RetrieveableSerializer):
  user = UserNameSerializer(read_only=True)

  class Meta:
    fields = ['id', 'user']