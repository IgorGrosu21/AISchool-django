from rest_framework.serializers import ModelSerializer, UUIDField

from ..user import UserSerializer

class PersonSerializer(ModelSerializer):
  id = UUIDField()
  user = UserSerializer(read_only=True)