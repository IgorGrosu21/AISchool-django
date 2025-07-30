from rest_framework import generics
from drf_spectacular.utils import extend_schema
from auth.models import AuthUser
from auth.serializers import SignUpSerializer, LoginSerializer

class AuthView(generics.CreateAPIView):
  queryset = AuthUser.objects.all()
  authentication_classes = []
  permission_classes = []
  
@extend_schema(tags=['auth / auth'])
class SignUpView(AuthView):
  serializer_class = SignUpSerializer

@extend_schema(tags=['auth / auth'])
class LoginView(AuthView):
  serializer_class = LoginSerializer