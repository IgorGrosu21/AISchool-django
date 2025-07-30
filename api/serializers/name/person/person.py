from rest_framework.serializers import ModelSerializer

from ..user import UserNameSerializer

class PersonNameSerializer(ModelSerializer):
  user = UserNameSerializer(read_only=True)