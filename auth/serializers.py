from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import AuthUser

class AuthUserSerializer(ModelSerializer):
  class Meta:
    model = AuthUser
    fields = ['email', 'password']
    read_only_fields = ['password']

class AuthTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    token['key'] = user.key
    return token