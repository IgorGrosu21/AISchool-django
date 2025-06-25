from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from auth.models import AuthUser
from auth.serializers import SignUpSerializer, LoginSerializer

class AuthView(generics.CreateAPIView):
  queryset = AuthUser.objects.all()
  authentication_classes = []
  permission_classes = []
  
  def create(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data, context={'request': request})
    if serializer.is_valid():
      user = serializer.save()
      refresh = RefreshToken.for_user(user)
      access = refresh.access_token
      return Response({'access': str(access), 'refresh': str(refresh)}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SignUpView(AuthView):
  serializer_class = SignUpSerializer

class LoginView(AuthView):
  serializer_class = LoginSerializer