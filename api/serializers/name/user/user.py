from rest_framework.serializers import ModelSerializer

from api.models import User

class UserNameSerializer(ModelSerializer):
  class Meta:
    fields = ['id', 'name', 'surname', 'profile_link']
    model = User