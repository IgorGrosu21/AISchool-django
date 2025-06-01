from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import AuthUser
from .serializers import SignUpSerializer, LoginSerializer
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

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
    
class LogoutView(APIView):
  def post(self, request):
    refresh_token = request.data.get('refresh')
    if not refresh_token:
      return Response({'error': 'no_refresh_token'}, status=status.HTTP_400_BAD_REQUEST)

    try:
      token = RefreshToken(refresh_token)
      token.blacklist()
    except Exception as e:
      return Response({'error': 'invalid_refresh_token'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(None, status=status.HTTP_204_NO_CONTENT)

class LogoutAllView(APIView):
  def post(self, request):
    tokens = OutstandingToken.objects.filter(user=request.user)
    for token in tokens:
      BlacklistedToken.objects.get_or_create(token=token)
    return Response(None, status=status.HTTP_204_NO_CONTENT)

class RefreshTokenView(APIView):
  authentication_classes = []
  permission_classes = []

  def post(self, request):
    refresh_token = request.data.get('refresh')
    if not refresh_token:
      return Response({'error': 'no_refresh_token'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
      refresh = RefreshToken(refresh_token)
      access = refresh.access_token
      return Response({'access': str(access)}, status=status.HTTP_200_OK)
    except Exception as e:
      return Response({'error': 'invalid_refresh_token'}, status=status.HTTP_400_BAD_REQUEST)
    
class WorkerView(APIView):
  authentication_classes = []
  permission_classes = []
  
  def get(self, request):
    return Response()