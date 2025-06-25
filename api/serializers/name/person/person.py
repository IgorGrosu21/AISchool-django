from rest_framework.serializers import ModelSerializer, UUIDField

from ..user import UserNameSerializer

class PersonNameSerializer(ModelSerializer):
  id = UUIDField()
  user = UserNameSerializer()