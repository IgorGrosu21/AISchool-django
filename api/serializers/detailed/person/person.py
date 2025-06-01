from rest_framework.serializers import ModelSerializer

from ..user import DetailedUserSerializer

class DetailedPersonSerializer(ModelSerializer):
  user = DetailedUserSerializer(read_only=True)