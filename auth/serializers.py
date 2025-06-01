from django.contrib.auth import authenticate
from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from .models import AuthUser

class AuthSerializer(ModelSerializer):
  email = CharField(validators=[])
  password = CharField(write_only=True)
  
  class Meta:
    model = AuthUser
    fields = ['email', 'password']

class SignUpSerializer(AuthSerializer):
  def validate_email(self, value: str):
    if AuthUser.objects.filter(email=value).exists():
      raise ValidationError('email_already_exists')
    return value
  
  def validate_password(self, value: str):
    if len(value) < 8:
      raise ValidationError('password_too_small')
    elif value.isdigit():
      raise ValidationError('password_only_numbers')
    elif value.isalpha():
      raise ValidationError('password_only_letters')
    return value
  
  def create(self, validated_data):
    return AuthUser.objects.create_user(**validated_data)
  
class LoginSerializer(AuthSerializer):
  def validate_email(self, value: str):
    if not AuthUser.objects.filter(email=value).exists():
      raise ValidationError('email_not_found')
    return value

  def validate_password(self, value: str):
    request = self.context['request']
    
    try:
      email = self.validate_email(request.data.get('email'))
      user = authenticate(request, email=email, password=value)
      if not user:
        raise ValidationError('password_incorect')
    finally:
      return value
  
  def create(self, validated_data):
    return AuthUser.objects.get(email=validated_data.get('email'))