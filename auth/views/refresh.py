from functools import wraps
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

def with_valid_refresh_token(view_func):
  @wraps(view_func)
  def wrapped(self, request, *args, **kwargs):
    refresh_token = request.data.get('refresh')
    if not refresh_token:
      return Response({'error': 'no_refresh_token'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
      request.refresh_token = RefreshToken(refresh_token)
      return view_func(self, request, *args, **kwargs)
    except Exception as e:
      return Response({'error': 'invalid_refresh_token'}, status=status.HTTP_400_BAD_REQUEST)
  
  return wrapped

class RefreshTokenView(APIView):
  authentication_classes = []
  permission_classes = []
  
  @with_valid_refresh_token
  def post(self, request, *args, **kwargs):
    access = request.refresh_token.access_token
    return Response({'access': str(access)}, status=status.HTTP_200_OK)
    
class LogoutView(APIView):
  @with_valid_refresh_token
  def post(self, request, *args, **kwargs):
    request.refresh_token.blacklist()
    return Response(None, status=status.HTTP_204_NO_CONTENT)

class LogoutAllView(APIView):
  def post(self, request):
    tokens = OutstandingToken.objects.filter(user=request.user)
    for token in tokens:
      BlacklistedToken.objects.get_or_create(token=token)
    return Response(None, status=status.HTTP_204_NO_CONTENT)