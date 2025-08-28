import re
from django.contrib.auth import authenticate
from rest_framework.serializers import ModelSerializer, Serializer, CharField, ValidationError, SerializerMethodField
from rest_framework_simplejwt.tokens import RefreshToken
from .models import AuthUser

#refresh
class AccessTokenSerializer(Serializer):
  access = CharField(read_only=True)

#auth
class AuthSerializer(ModelSerializer):
  email = CharField(validators=[], write_only=True)
  password = CharField(write_only=True)
  access = SerializerMethodField()
  refresh = SerializerMethodField()
  
  def create_tokens(self, user: AuthUser):
    refresh = RefreshToken.for_user(user)
    self._tokens = { 'access': str(refresh.access_token), 'refresh': str(refresh) }
    return user
  
  def get_access(self, _) -> str:
    return self._tokens.get('access', '')
  
  def get_refresh(self, _) -> str:
    return self._tokens.get('refresh', '')

  class Meta:
    model = AuthUser
    fields = ['email', 'password', 'access', 'refresh']

class SignUpSerializer(AuthSerializer):
  def validate_email(self, value: str):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_pattern, value):
        raise ValidationError('invalid_email_format')
    
    domain = value.split('@')[1]
    if len(domain) < 3 or '.' not in domain:
        raise ValidationError('invalid_email_domain')
    
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
    user = AuthUser.objects.create_user(**validated_data)
    return self.create_tokens(user)
  
class LoginSerializer(AuthSerializer):
  def validate_email(self, value: str):
    if not AuthUser.objects.filter(email=value).exists():
      raise ValidationError('email_not_found')
    return value

  def validate_password(self, value: str):
    request = self.context['request']
    email = None
    
    try:
      email = self.validate_email(request.data.get('email'))
    finally:
      if email:
        user = authenticate(request, email=email, password=value)
        if user == None:
          raise ValidationError('password_incorect')
      return value
  
  def create(self, validated_data):
    try:
      user = AuthUser.objects.get(email=validated_data.get('email'))
      return self.create_tokens(user)
    except AuthUser.DoesNotExist:
      raise ValidationError('email_not_found')